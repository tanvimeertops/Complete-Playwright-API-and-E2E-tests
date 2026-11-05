# Northline Store – Playwright Automation

## Tech Stack
- Python
- Playwright
- Pytest
- Pytest HTML Report

## Project Structure
- pages/ – Page Object Model classes
- tests/api/ – API test cases
- tests/e2e/ – End-to-end test cases
- data/ – Test data and JSON schema
- reports/ – HTML test reports

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium