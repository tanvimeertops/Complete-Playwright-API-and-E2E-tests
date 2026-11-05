import re
import pytest
from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage


def add_first_product_to_cart(page):
    page.goto("/products")

    product_cards = page.locator("a[href^='/products/']")
    expect(product_cards.first).to_be_visible(timeout=10000)

    product_cards.first.click()
    page.wait_for_url(re.compile(r"/products/.+"))

    add_button = page.get_by_role(
        "button",
        name=re.compile(r"add\s*to\s*cart", re.I)
    )

    expect(add_button).to_be_visible()
    add_button.click()


@pytest.mark.e2e
def test_checkout_empty_fields_validation(page):
    add_first_product_to_cart(page)

    checkout = CheckoutPage(page)
    checkout.navigate()
    checkout.continue_to_review()

    errors = page.get_by_text(
        re.compile(r"(required|is required)", re.I)
    )

    expect(errors.first).to_be_visible(timeout=5000)


@pytest.mark.e2e
def test_checkout_missing_postal_code(page):
    add_first_product_to_cart(page)

    checkout = CheckoutPage(page)
    checkout.navigate()
    checkout.fill_shipping_details(postal_code="")
    checkout.continue_to_review()

    postal_error = page.get_by_text(
        re.compile(r"postal\s*code\s*is\s*required", re.I)
    )

    expect(postal_error).to_be_visible(timeout=5000)


@pytest.mark.e2e
def test_checkout_valid_submission(page):
    add_first_product_to_cart(page)

    checkout = CheckoutPage(page)
    checkout.navigate()
    checkout.fill_shipping_details()
    checkout.continue_to_review()

    expect(checkout.place_order_button).to_be_visible(timeout=10000)
    checkout.place_order()

    confirmation = page.get_by_text(
        re.compile(r"(order\s*confirmed|thank\s*you)", re.I)
    )

    expect(confirmation.first).to_be_visible(timeout=10000)