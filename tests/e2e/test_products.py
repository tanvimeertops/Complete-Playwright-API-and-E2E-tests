import pytest
from playwright.sync_api import expect
from pages.product_listing_page import ProductListingPage


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