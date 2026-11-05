from playwright.sync_api import Page, expect


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page
        self.register_heading = page.get_by_role(
            "heading", name="Create your account"
        )

    def navigate(self):
        self.page.goto("/register")

    def verify_register_page(self):
        expect(self.register_heading).to_be_visible()