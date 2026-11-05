from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.checkout_heading = page.get_by_role(
            "heading", name="Checkout"
        )

    def navigate(self):
        self.page.goto("/checkout")

    def verify_checkout_page(self):
        expect(self.checkout_heading).to_be_visible()