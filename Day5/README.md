# Day 5 - Web Element Handling

## Scripts Overview

### 1. handle_brokenlinks.py
Tests website links to identify broken/invalid URLs using HTTP status codes.

**Key Features:**
- Uses `requests` library for HTTP status checking
- Finds all anchor tags with `find_elements(By.TAG_NAME, "a")`
- Checks each link's HTTP status code
- Identifies broken links (status code ≥ 400)
- Counts total broken links found

**Test Site:** http://www.deadlinkcity.com/

### 2. handle_chech_box.py
Demonstrates checkbox selection and deselection operations.

**Key Features:**
- Locates multiple checkboxes using XPath
- Selects all checkboxes in a loop
- Uses `is_selected()` to check checkbox state
- Deselects all previously selected checkboxes

**Test Site:** https://testautomationpractice.blogspot.com/

### 3. handle_dropdown.py
Shows dropdown menu interaction using Select class.

**Key Features:**
- `Select` class for dropdown handling
- `select_by_visible_text()` - Select by display text
- `select_by_value()` - Select by value attribute (commented)
- `select_by_index()` - Select by position (commented)
- Lists all dropdown options with `.options`

**Test Site:** https://practice.expandtesting.com/dropdown

### 4. handle_links.py
Extracts and displays all link texts from a webpage.

**Key Features:**
- Finds all anchor tags on the page
- Extracts text content from each link
- Demonstrates link text retrieval
- Includes commented link clicking example

**Test Site:** https://demo.nopcommerce.com/

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver
- requests library (`pip install requests`)

## Usage
```bash
python handle_brokenlinks.py
python handle_chech_box.py
python handle_dropdown.py
python handle_links.py
```