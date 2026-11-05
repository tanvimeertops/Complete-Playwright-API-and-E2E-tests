from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_heading = page.get_by_role("heading", name="Welcome back")
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Sign in")

    def navigate(self):
        self.page.goto("/login")

    def verify_login_page(self):
        expect(self.login_heading).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()