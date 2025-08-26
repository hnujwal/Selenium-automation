# Day 3 - Selenium WebDriver Commands

## Scripts Overview

### 1. Browser_coomends.py
Demonstrates browser navigation and window management commands.

**Commands Used:**
- `driver.get()` - Navigate to URLs
- `driver.maximize_window()` - Maximize browser window
- `driver.back()` - Navigate back
- `driver.forward()` - Navigate forward
- `driver.refresh()` - Refresh page
- `driver.quit()` - Close browser

**Test Flow:**
- Opens Amazon website
- Navigates to Flipkart
- Maximizes window
- Tests back/forward navigation
- Refreshes page

### 2. Conditional_commends.py
Tests element state verification methods.

**Commands Used:**
- `is_displayed()` - Check if element is visible
- `is_enabled()` - Check if element is enabled
- `find_element()` - Locate single element

**Test Actions:**
- Verifies search box visibility and state
- Clicks Register link

### 3. Application_commends.py
Application-level command demonstrations.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver

## Usage
```bash
python Browser_coomends.py
python Conditional_commends.py
python Application_commends.py
```