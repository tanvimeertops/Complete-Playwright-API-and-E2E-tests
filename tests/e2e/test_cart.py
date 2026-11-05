import pytest
from pages.cart_page import CartPage


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