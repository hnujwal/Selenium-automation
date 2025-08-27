# Day 4 - Selenium Wait Strategies

## Scripts Overview

### 1. explicitly_wait.py
Demonstrates explicit wait using WebDriverWait and Expected Conditions.

**Key Features:**
- `WebDriverWait(driver, 10)` - Sets maximum wait time
- `EC.visibility_of_element_located()` - Waits for element visibility
- Waits for username and password fields before interaction
- OrangeHRM login test with explicit waits

### 2. implicitly_wait.py
Shows implicit wait implementation for automatic element waiting.

**Key Features:**
- `driver.implicitly_wait(10)` - Global wait for all elements
- Searches for laptop on nopCommerce
- Clicks on laptop product link
- Automatic waiting for all find_element operations

### 3. Time_coomends.py
Uses Python's time.sleep() for fixed delays.

**Key Features:**
- `time.sleep(5)` - Fixed 5-second pause
- Hard-coded wait regardless of element availability
- Same laptop search functionality as implicit wait

## Wait Strategy Comparison

| Wait Type | Usage | Pros | Cons |
|-----------|-------|------|------|
| **Explicit** | Specific conditions | Precise control | More code |
| **Implicit** | Global setting | Simple setup | Less flexible |
| **Sleep** | Fixed delays | Easy to use | Inefficient |

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver

## Usage
```bash
python explicitly_wait.py
python implicitly_wait.py
python Time_coomends.py
```

## Test URLs
- https://opensource-demo.orangehrmlive.com (explicit wait)
- https://demo.nopcommerce.com (implicit wait & sleep)