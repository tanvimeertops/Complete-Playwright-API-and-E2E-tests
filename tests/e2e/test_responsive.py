import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_mobile_viewport_layout(page):
    page.set_viewport_size({"width": 390, "height": 844})

    # Home page
    page.goto("/")
    expect(page).to_have_title("Northline Store")
    expect(page.locator("header")).to_be_visible()

    # Products page
    page.goto("/products")
    product = page.locator("main a[href^='/products/']").first
    expect(product).to_be_visible()

    # Product detail
    product.click()
    expect(page.locator("main h1")).to_be_visible()

    # Add to cart
    page.get_by_role("button", name="Add to cart").click()

    # Cart page
    page.goto("/cart")
    expect(page.locator("main")).to_contain_text("$")

    # Check horizontal overflow
    body_width = page.locator("body").evaluate(
        "(element) => element.scrollWidth"
    )
    assert body_width <= 390, f"Horizontal overflow: {body_width}px"