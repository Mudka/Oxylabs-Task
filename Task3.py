from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=true")  
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

url = "https://www.bing.com/search?q=pikachu&form=QBLH&sp=-1&lq=0&pq=pikachu&sc=12-7&qs=n&sk=&cvid=F4FDC17B1E63458CBF79D7A4C40C6C42&ghsh=0&ghacc=0&ghpl="

driver.get(url)

time.sleep(5)

html = driver.page_source

with open("bing_pikachu.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.quit()
print("HTML saved as 'bing_pikachu.html'")