# Day 7 - Advanced Selenium Actions

## Scripts Overview

### 1. Upload_file.py
Demonstrates file upload functionality using send_keys method.

**Key Features:**
- File input element location by ID
- Direct file path upload using `send_keys()`
- Success confirmation message
- Simple and clean file upload implementation

**Test Site:** https://testautomationpractice.blogspot.com/

### 2. Mouse_Action.py
Comprehensive mouse actions using ActionChains class.

**Key Features:**
- **Mouse Hover:** Multi-level menu navigation
- **Drag & Drop:** Element dragging between containers
- **Double Click:** Double-click action on elements
- **Right Click:** Context menu triggering
- **Scrolling:** JavaScript scroll to bottom

**Test Site:** https://vinothqaacademy.com/mouse-event/

### 3. scroll_down.py
Different scrolling techniques for web page navigation.

**Key Features:**
- `window.scrollBy(0, 1000)` - Scroll by pixels (commented)
- `scrollIntoView()` - Scroll to specific element (commented)
- `window.scrollBy(0, document.body.scrollHeight)` - Scroll to bottom

**Test Site:** https://www.awwwards.com/websites/scrolling/

### 4. table.py
Web table data extraction and processing.

**Key Features:**
- Dynamic table row and column counting
- Nested loops for table traversal
- Cell data extraction using XPath
- Formatted table data display

**Test Site:** https://www.w3.org/WAI/UA/2002/06/thead-test

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver

## Usage
```bash
python Upload_file.py
python Mouse_Action.py
python scroll_down.py
python table.py
```

## Action Types Covered
- File uploads
- Mouse hover chains
- Drag and drop operations
- Click actions (single, double, right-click)
- Page scrolling methods
- Table data extraction