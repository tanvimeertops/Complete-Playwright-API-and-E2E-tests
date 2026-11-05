import re
from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.address = page.locator("#line1")
        self.city = page.locator("#city")
        self.state = page.locator("#state")
        self.postal_code = page.locator("#postalCode")

        self.continue_button = page.get_by_role(
            "button",
            name=re.compile(r"continue\s*to\s*review", re.I)
        )

        self.place_order_button = page.get_by_role(
            "button",
            name=re.compile(r"place\s*order", re.I)
        )

    def navigate(self):
        self.page.goto("/checkout")
        self.page.wait_for_load_state("networkidle")

    def fill_shipping_details(self, postal_code="10001"):
        self.address.fill("123 Test Street")
        self.city.fill("New York")
        self.state.fill("NY")
        self.postal_code.fill(postal_code)

    def continue_to_review(self):
        self.continue_button.click()

    def place_order(self):
        self.place_order_button.click()