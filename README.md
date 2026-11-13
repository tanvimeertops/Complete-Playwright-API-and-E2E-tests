Northline Store – Playwright Automation

Automated UI and API testing framework for the Northline Store e-commerce application using Python, Playwright and pytest.

Target Application: https://ecomcicid.netlify.app/

1. Tech Stack

Technology| Purpose
Python| Programming language
Playwright| Browser automation
Pytest| Test execution
Pytest HTML| Test reporting
Requests / Playwright API| API testing
JSON Schema| API response validation
Git & GitHub| Version control
GitHub Actions| CI/CD workflow

2. Project Structure

northline-tests/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── data/
│   ├── product_schema.json
│   └── test_data.json
│
├── pages/
│   ├── home_page.py
│   ├── product_listing_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── register_page.py
│
├── tests/
│   ├── api/
│   │   └── test_products.py
│   │
│   └── e2e/
│       ├── test_home.py
│       ├── test_products.py
│       ├── test_product_detail.py
│       ├── test_cart.py
│       ├── test_checkout.py
│       ├── test_register.py
│       ├── test_login.py
│       ├── test_negative.py
│       ├── test_persistence.py
│       └── test_responsive.py
│
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

3. Setup and Installation

Clone the repository

git clone <your-repository-url>
cd northline-tests

Create virtual environment

python -m venv .venv
.venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Install Playwright browser

playwright install chromium

4. Running Tests

Run all tests

pytest

Run API tests

pytest tests/api -v

Run E2E tests

pytest tests/e2e -v

Run smoke tests

pytest -m smoke

Run tests by marker

pytest -m e2e
pytest -m api

Run a specific test file

pytest tests/e2e/test_cart.py -v

Run browser in headed mode

pytest --headed

5. Test Coverage

End-to-End Testing

- Home page and navigation
- Product listing and product details
- Product search and filtering
- Product sorting
- Add products to cart
- Update cart quantity
- Remove products from cart
- Empty cart validation
- Checkout form validation
- Order confirmation
- Cart persistence after reload
- Responsive mobile viewport
- Invalid URL handling

API Testing

- GET product list
- GET individual product
- Product response validation
- Product schema validation
- Invalid product ID handling
- HTTP response validation
- Response time checks

6. Reports and Debugging

Generate an HTML report:

pytest --html=reports/report.html --self-contained-html

The report can be opened in a browser to review test results.

Playwright traces and screenshots can be used to investigate failed tests when configured in pytest settings.

7. CI/CD

GitHub Actions workflow is maintained at:

.github/workflows/tests.yml

The workflow is used to automate test execution through GitHub Actions. Refer to the workflow configuration for its actual triggers, browser configuration and artifact settings.

8. Page Object Model

This project follows the Page Object Model (POM) design pattern.

- Page locators and page-related actions are maintained in the "pages/" directory.
- Test scenarios are maintained separately in the "tests/" directory.
- Shared fixtures and configurations are maintained in "conftest.py".

This separation improves code organization, maintainability and reusability.

9. Version Control

Git and GitHub are used to maintain project source code and track changes.

---

Project: Northline Store – Playwright Automation
Language: Python
Framework: Playwright + Pytest