import pytest
from pages.cart_page import CartPage
from playwright.sync_api import expect


@pytest.mark.e2e
def test_cart_page_loads(page):
    cart = CartPage(page)
    cart.navigate()
    cart.verify_cart_page()


@pytest.mark.e2e
def test_empty_cart_message(page):
    cart = CartPage(page)
    cart.navigate()
    cart.verify_cart_empty()

@pytest.mark.e2e
def test_change_quantity(page):
    page.goto("/products")
    page.locator("main a[href^='/products/']").first.click()
    page.get_by_role("button", name="Add to cart").click()
    page.goto("/cart")

    increase = page.get_by_role("button", name="Increase quantity")
    increase.click()

    expect(page.get_by_text("2", exact=True)).to_be_visible()
    expect(page.locator("main")).to_contain_text("$330.00")


@pytest.mark.e2e
def test_remove_item_from_cart(page):
    page.goto("/products")
    page.locator("main a[href^='/products/']").first.click()
    page.get_by_role("button", name="Add to cart").click()
    page.goto("/cart")

    page.get_by_role("button", name="Remove").click()

    expect(page.get_by_text("Your cart is empty.")).to_be_visible()