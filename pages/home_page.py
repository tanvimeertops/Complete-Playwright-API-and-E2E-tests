from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.logo = page.get_by_role("link", name="Northline")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.products_link = page.get_by_role("link", name="Products", exact=True)

    def navigate(self):
        self.page.goto("/")

    def click_logo(self):
        self.logo.click()

    def open_cart(self):
        self.cart_link.click()

    def open_products(self):
        self.products_link.click()