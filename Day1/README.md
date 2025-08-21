# FirstTestcase.py

## Description
A Selenium WebDriver test script that automates login functionality for the OrangeHRM demo application.

## Test Scenario
- Opens Chrome browser
- Navigates to OrangeHRM demo login page
- Enters credentials (Admin/admin123)
- Clicks login button
- Verifies page title matches expected value

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver

## Installation
```bash
pip install selenium
```

## Usage
```bash
python FirstTestcase.py
```

## Expected Output
- "Login test passed" if title verification succeeds
- "loin test failed" if title verification fails

## Test URL
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login