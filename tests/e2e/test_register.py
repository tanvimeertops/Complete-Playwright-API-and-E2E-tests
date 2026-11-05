import pytest
from pages.register_page import RegisterPage


@pytest.mark.e2e
def test_register_page_loads(page):
    register = RegisterPage(page)
    register.navigate()
    register.verify_register_page()