import re
import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_invalid_url_handling(page):
    response = page.goto("/this-page-does-not-exist-xyz123")

    assert response is not None
    assert response.status == 200

    expect(page).to_have_title(re.compile("Northline", re.I))
    expect(page.locator("#root")).to_be_attached()