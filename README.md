markdown
# Yandex.Samokat — API Test Automation

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-7.4+-orange.svg)](https://docs.pytest.org/)
[![requests](https://img.shields.io/badge/requests-2.31+-green.svg)](https://docs.python-requests.org/)
[![Allure](https://img.shields.io/badge/Allure-2.13-purple.svg)](https://docs.qameta.io/allure/)

Automated API tests for [Yandex.Samokat](https://qa-scooter.praktikum-services.ru/) — a scooter rental service.  
The project covers courier creation, login, order placement, and order list retrieval.

## Project Description

This project contains automated API tests built with **pytest** and the **requests** library.  
It uses **Allure** for detailed test reports and follows a structured approach with separate helpers for endpoints and data generation.

## Test Coverage

### Courier Creation
- Positive scenario: courier can be created
- Negative scenarios:
  - Cannot create two identical couriers
  - Missing required fields return error
  - Login already exists returns error

### Courier Login
- Positive scenario: courier can log in
- Negative scenarios:
  - Login with incorrect login/password
  - Missing required fields
  - Non‑existent user

### Order Creation
- Parameterized test for color selection:
  - BLACK only
  - GREY only
  - Both colors
  - No color

### Order List
- Verify that response contains a list of orders

## Bug Found

While testing the login endpoint, the following discrepancy was discovered:

| Expected | Actual |
|----------|--------|
| According to API documentation, attempting to login without the required `password` field should return `400 Bad Request`. | The server returns `504 Gateway Timeout`. |

## Project Structure

```
Yandex-Samokat-API-Tests/
    ├── README.md
    ├── conftest.py
    ├── .gitignore
    ├── requirements.txt
    ├── allure_results/
    ├── helpers/
    │   ├── api_helpers.py
    │   ├── courier_helper.py
    │   └── endpoints.py
    └── tests/
        ├── test_create_courier.py
        ├── test_create_order.py
        ├── test_get_orders.py
        └── test_login_courier.py

    ``` 

## Setup & Installation

### Requirements
- Python 3.12+
- pytest
- requests
- allure-pytest

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/nvbeznosova/Yandex-Samokat-API-Tests.git
   cd Yandex-Samokat-API-Tests
   ```

2. **Create and activate a virtual environment** 
```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   # .venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
   ``` 

## Running tests

1. **Run all tests**
```bash
   pytest tests/
   ``` 
2. **Run a specific test file**
```bash
   pytest tests/test_create_courier.py
   ``` 
3. **Run with verbose output**
```bash
   pytest -v tests/
   ``` 
## Allure Reports

**To generate and view an Allure report locally**

1. **Run tests with Allure enabled**
```bash
   pytest --alluredir=allure-results tests/
   ```

2. **Generate and open the report**
```bash
   allure serve allure-results
   ```
In CI/CD (GitHub Actions) the report can be automatically published to GitHub Pages. 
