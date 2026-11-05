from playwright.sync_api import Page, expect


class ProductListingPage:

    def __init__(self, page: Page):
        self.page = page
        self.product_cards = page.locator("main a[href^='/products/']")

    def navigate(self):
        self.page.goto("/products")

    def verify_products_visible(self):
        expect(self.product_cards.first).to_be_visible()
        expect(self.product_cards).to_have_count(6)

    def filter_by_category(self, category):
        self.page.get_by_role("button", name=category, exact=True).click()