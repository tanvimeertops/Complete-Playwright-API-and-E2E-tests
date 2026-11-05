from playwright.sync_api import Page, expect


class ProductDetailPage:

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("main h1")
        self.add_to_cart_button = page.get_by_role(
            "button", name="Add to cart"
        )

    def navigate(self):
        self.page.goto("/products/organic-cotton-overshirt")

    def verify_product_details(self):
        expect(self.product_title).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()

    def add_to_cart(self):
        self.add_to_cart_button.click()