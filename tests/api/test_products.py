import pytest
import time
import json
from pathlib import Path
from jsonschema import validate

@pytest.mark.api
def test_get_all_products(api_context):

    response = api_context.get("/electronicapi")

    assert response.status == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0

    print("Total products:", len(data))


# API-02: Get single product
@pytest.mark.api
def test_get_single_product(api_context):

    response = api_context.get("/electronicapi/1")

    assert response.status == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == "1"
    assert data["name"] == "Skullcandy Crusher Evo"
    assert data["price"] == "19200"

    print("Product name:", data["name"])
    print("Product price:", data["price"])

# API-03: Get unknown product ID
@pytest.mark.api
def test_get_invalid_product(api_context):

    response = api_context.get("/electronicapi/9999")

    assert response.status == 404

    print("Status code:", response.status)

# API-04: Response time
@pytest.mark.api
def test_product_response_time(api_context):

    start_time = time.perf_counter()

    response = api_context.get("/electronicapi")

    end_time = time.perf_counter()

    response_time = end_time - start_time

    assert response.status == 200
    assert response_time < 2

    print("Response time:", round(response_time, 3), "seconds")


# API-05: Validate response headers
@pytest.mark.api
def test_product_response_headers(api_context):

    response = api_context.get("/electronicapi")

    assert response.status == 200

    headers = response.headers

    assert "application/json" in headers["content-type"]

    print("Content-Type:", headers["content-type"])

# API-06: JSON Schema Validation
@pytest.mark.api
def test_product_schema(api_context):

    response = api_context.get("/electronicapi/1")

    assert response.status == 200

    data = response.json()

    schema_path = Path(__file__).parents[2] / "data" / "product_schema.json"

    with open(schema_path, "r") as file:
        schema = json.load(file)

    validate(instance=data, schema=schema)

    print("Product JSON schema validation successful")

# API-07: Validate product fields and data types
@pytest.mark.api
def test_product_fields(api_context):

    response = api_context.get("/electronicapi/1")

    assert response.status == 200

    data = response.json()

    assert isinstance(data["id"], str)
    assert isinstance(data["name"], str)
    assert isinstance(data["price"], str)
    assert isinstance(data["brand"], str)
    assert isinstance(data["category"], str)
    assert isinstance(data["rating"], str)
    assert isinstance(data["stock"], str)

    assert data["name"] != ""
    assert data["price"] != ""
# API-08: Validate product count and data
@pytest.mark.api
def test_product_count_and_data(api_context):

    response = api_context.get("/electronicapi")

    assert response.status == 200

    products = response.json()

    assert len(products) > 0

    product_ids = [product["id"] for product in products]

    assert len(product_ids) == len(set(product_ids))

    for product in products:
        assert product["name"] != ""
        assert product["price"] != ""

    print("Total products:", len(products))
    print("Product data validation successful")


