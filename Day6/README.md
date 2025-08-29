# Day 6 - Selenium Window & Popup Handling

## Scripts Overview

### 1. handle_browser_windows.py
Demonstrates handling multiple browser windows and switching between them.

**Key Features:**
- Opens OrangeHRM login page
- Clicks link that opens new window
- `driver.window_handles` - Gets all window IDs
- `driver.switch_to.window()` - Switches between windows
- Loops through all windows and prints titles

### 2. handle_alert_window.py
Shows JavaScript alert handling with user input.

**Key Features:**
- `driver.switch_to.alert` - Access alert popup
- `alert.text` - Read alert message
- `alert.send_keys()` - Input text in prompt
- `alert.accept()` / `alert.dismiss()` - Accept/Cancel alert

### 3. handle_authentication_popup.py
Handles HTTP basic authentication popup.

**Key Features:**
- URL format: `https://username:password@domain.com`
- Bypasses authentication popup by embedding credentials in URL
- Direct authentication without popup interaction

### 4. handle_iframe.py
Demonstrates iframe switching and nested iframe handling.

**Key Features:**
- `driver.switch_to.frame()` - Switch to iframe by name/element
- `driver.switch_to.default_content()` - Return to main page
- Handles multiple iframes on same page
- Nested iframe navigation (iframe within iframe)

## Window/Popup Types Covered

| Type | Method | Use Case |
|------|--------|----------|
| **Browser Windows** | `window_handles` | Multiple tabs/windows |
| **JavaScript Alerts** | `switch_to.alert` | Confirmation dialogs |
| **Authentication** | URL credentials | HTTP basic auth |
| **iFrames** | `switch_to.frame()` | Embedded content |

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver

## Usage
```bash
python handle_browser_windows.py
python handle_alert_window.py
python handle_authentication_popup.py
python handle_iframe.py
```

## Test URLs
- https://opensource-demo.orangehrmlive.com (browser windows)
- https://the-internet.herokuapp.com/javascript_alerts (alerts)
- https://the-internet.herokuapp.com/basic_auth (authentication)
- https://vinothqaacademy.com/iframe/ (iframes)
- https://demo.automationtesting.in/Frames.html (nested iframes)