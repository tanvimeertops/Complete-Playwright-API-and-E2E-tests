import pytest
from pages.login_page import LoginPage


@pytest.mark.e2e
def test_login_page_loads(page):
    login = LoginPage(page)
    login.navigate()
    login.verify_login_page()