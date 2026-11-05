import pytest
from playwright.sync_api import expect
from pages.product_listing_page import ProductListingPage
import re

@pytest.mark.smoke
@pytest.mark.e2e
def test_products_page_loads(page):
    products = ProductListingPage(page)
    products.navigate()

    expect(page).to_have_url("https://ecomcicid.netlify.app/products")
    expect(page).to_have_title("Northline Store")


@pytest.mark.e2e
def test_products_are_displayed(page):
    products = ProductListingPage(page)
    products.navigate()

    products.verify_products_visible()

@pytest.mark.e2e
def test_filter_products_by_category(page):
    products = ProductListingPage(page)
    products.navigate()
    products.filter_by_category("Living")

    expect(products.product_cards).to_have_count(4)

@pytest.mark.e2e
def test_sort_products_by_newest(page):
    products = ProductListingPage(page)
    products.navigate()

    page.get_by_role("button", name="Newest").click()

    expect(products.product_cards).to_have_count(6)
@pytest.mark.smoke
@pytest.mark.e2e
def test_product_listing_details(page):
    products = ProductListingPage(page)
    products.navigate()

    first = products.product_cards.first
    expect(first.locator("img").first).to_be_visible()
    expect(first).to_contain_text(re.compile(r"\$\d"))
    assert first.inner_text().strip()


@pytest.mark.e2e
def test_search_known_product(page):
    page.goto("/products?search=overshirt")

    cards = page.locator("main a[href^='/products/']")
    expect(cards.first).to_be_visible()

    for i in range(cards.count()):
        assert "overshirt" in cards.nth(i).inner_text().lower()


@pytest.mark.e2e
def test_search_nonsense_term(page):
    page.goto("/products?search=xyzzyplughqwerty12345")

    expect(
        page.get_by_text(re.compile(r"no\s*(results|products|items)", re.I))
    ).to_be_visible()


@pytest.mark.e2e
def test_sort_price_low_to_high(page):
    page.goto("/products")
    page.get_by_role("button", name="Newest").click()

    page.get_by_text(
        re.compile(r"Price:\s*low to high", re.I)
    ).click()

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)

    cards = page.locator("main a[href^='/products/']")
    prices = []

    for i in range(cards.count()):
        card_text = cards.nth(i).inner_text()
        matches = re.findall(r"\$(\d+(?:\.\d{2})?)", card_text)

        if matches:
            prices.append(float(matches[-1]))

    assert len(prices) >= 2
    assert prices == sorted(prices)