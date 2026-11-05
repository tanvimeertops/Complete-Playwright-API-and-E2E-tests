import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.e2e
@pytest.mark.smoke
def test_home_page_loads(page):

    home = HomePage(page)
    home.navigate()

    expect(page).to_have_title("Northline Store")


# E2E-02: Verify Products navigation
@pytest.mark.e2e
def test_products_navigation(page):

    home = HomePage(page)
    home.navigate()

    home.open_products()

    expect(page).to_have_url("https://ecomcicid.netlify.app/products")