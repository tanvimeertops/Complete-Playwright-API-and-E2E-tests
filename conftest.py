import pytest
from playwright.sync_api import APIRequestContext


@pytest.fixture(scope="session")
def api_context(playwright):
    api = playwright.request.new_context(
        base_url="https://681444af225ff1af16285b31.mockapi.io",
        extra_http_headers={
            "Accept": "application/json"
        }
    )

    yield api

    api.dispose()