import pytest
from pages.checkout_page import CheckoutPage


@pytest.mark.e2e
def test_checkout_page_loads(page):
    checkout = CheckoutPage(page)
    checkout.navigate()
    checkout.verify_checkout_page()