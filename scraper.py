from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔧 CHANGE THIS to use another browser like Chrome, Edge, etc.
# For Brave users only (you can change to chrome.exe path or leave it out for default Chrome)
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# 🎛️ Browser options
options = webdriver.ChromeOptions()
options.binary_location = brave_path  # Change or comment if using Chrome
# options.add_argument("--headless")  # Uncomment to run headless (no browser window)

# ⚙️ Start browser service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 🌐 CHANGE THIS to the website you want to scrape
target_url = "https://www.example.com" # <--PLACE YOUR TARGET URL
driver.get(target_url)

time.sleep(5)  # ⏳ Wait for the page to load (increase if site is slow)

# 📄 Get full HTML after JavaScript loads
webpage_source = driver.page_source

#for default to save file of that webpage on your pc so you don't have to request again and again you can use your localhost for scraping
# 💾 Save page to a file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(webpage_source)

driver.quit()
print("✅ Page source saved to output.html")
