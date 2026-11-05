import pytest
from pages.product_detail_page import ProductDetailPage
from playwright.sync_api import expect
import re

@pytest.mark.e2e
def test_product_detail_page(page):
    product = ProductDetailPage(page)
    product.navigate()
    product.verify_product_details()


@pytest.mark.e2e
def test_add_product_to_cart(page):
    product = ProductDetailPage(page)
    product.navigate()
    product.add_to_cart()


@pytest.mark.smoke
@pytest.mark.e2e
def test_product_detail_shows_info(page):
    page.goto("/products")

    product_cards = page.locator(
        "[class*='product'], [class*='card'], article, li"
    ).filter(has=page.locator("img"))

    expect(product_cards.first).to_be_visible(timeout=10000)
    product_cards.first.locator("a, img, h2, h3, h4").first.click()

    page.wait_for_url(re.compile(r"/products/.+"))

    product_name = page.locator("h1, h2").first
    expect(product_name).to_be_visible()
    assert len(product_name.inner_text().strip()) > 0

    expect(page.get_by_text(re.compile(r"\$\d+")).first).to_be_visible()
    expect(page.locator("p").first).to_be_visible()

    add_to_cart = page.get_by_role(
        "button", name=re.compile(r"add\s*to\s*cart", re.I)
    )
    expect(add_to_cart).to_be_visible()