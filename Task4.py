from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=true")  
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

for page in range(1, 101):
    print(f"Scraping page {page}...")
    
    url = f"https://www.amazon.de/s?k=Nike&page={page}"
    driver.get(url)
    
    time.sleep(5)  

    html = driver.page_source

    with open(f"amazon_page_{page}.html", "w", encoding="utf-8") as f:
        f.write(html)

driver.quit()

print("Finished scraping 100 pages from Amazon.de")