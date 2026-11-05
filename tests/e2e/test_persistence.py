import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_cart_data_after_reload(page):
    page.goto("/products")

    product = page.locator("main a[href^='/products/']").first
    product.click()

    product_name = page.locator("main h1").inner_text()

    page.get_by_role("button", name="Add to cart").click()

    page.goto("/cart")

    expect(page.get_by_role("link", name=product_name)).to_be_visible()

    page.reload()

    expect(page.get_by_role("link", name=product_name)).to_be_visible()
    expect(page.locator("main")).to_contain_text("$")