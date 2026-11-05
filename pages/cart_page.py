from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_heading = page.get_by_role("heading", name="Cart")
        self.empty_message = page.get_by_text("Your cart is empty.")

    def navigate(self):
        self.page.goto("/cart")

    def verify_cart_page(self):
        expect(self.cart_heading).to_be_visible()

    def verify_cart_empty(self):
        expect(self.empty_message).to_be_visible()