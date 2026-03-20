# Browser Automation Scripts

Collection of browser automation scripts using Selenium.

## Setup

Install dependencies:

```bash
pip install selenium
```

You'll also need ChromeDriver installed. On most systems:

```bash
# Ubuntu/Debian
sudo apt-get install chromium-chromedriver

# macOS
brew install chromedriver

# Or download from: https://chromedriver.chromium.org/
```

## Scripts

### google_breakfast_search.py

Automates opening Google and searching for "breakfast".

**Usage:**
```bash
python google_breakfast_search.py
```

**Features:**
- Opens Google in Chrome
- Performs a search for "breakfast"
- Keeps browser open for 10 seconds to view results
- Can run headless (uncomment the headless option in the code)

## Requirements

- Python 3.6+
- Selenium
- ChromeDriver
- Chrome/Chromium browser
