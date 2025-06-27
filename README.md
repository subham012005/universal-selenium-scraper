# 🌐 Universal Selenium Scraper (with Brave)

This is a general-purpose web scraper using **Selenium** and **Brave browser** (or any browser).  
Use it to scrape the full HTML of any JavaScript-heavy website.

---

## 🚀 Features

- Uses `Selenium` with `webdriver-manager` (no manual driver download)
- Compatible with **Brave**, **Chrome**, or any Chromium-based browser
- Easy to modify: just change the `target_url`
- Saves fully rendered HTML to a local file

---

## 🔧 Requirements

```bash
pip install selenium webdriver-manager
```
## Also install the browser of your choice:
- Brave : https://brave.com/ 
- Google Chrome : https://www.google.com/chrome/

## 🛠 How to Use
Clone or download this repo

Open scraper.py

Change:

brave_path to your browser’s path (or remove for default Chrome)

target_url to the site you want to scrape

Run:
```bash
python scraper.py
```
After a few seconds, the script will save the rendered HTML as output.html.

⚙️ Browser Switch Example
To use Chrome instead of Brave, just:

Comment or delete this line:

```bash
options.binary_location = brave_path
```
Or set it to Chrome’s path:

```bash
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
```

## 🧠 Why Use Selenium?
Because some sites (like Flipkart, YouTube, LinkedIn) load data with JavaScript — and requests or BeautifulSoup won't see the real content. Selenium renders it like a real browser.

📌 Example
Change:
```bash
target_url = "https://www.flipkart.com"
```
And you're scraping Flipkart. Change to any site!
