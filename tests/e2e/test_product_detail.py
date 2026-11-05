import pytest
from pages.product_detail_page import ProductDetailPage


@pytest.mark.e2e
def test_product_detail_page(page):
    product = ProductDetailPage(page)
    product.navigate()
    product.verify_product_details()


@pytest.mark.e2e
def test_add_product_to_cart(page):
    product = ProductDetailPage(page)
    product.navigate()
    product.add_to_cart()