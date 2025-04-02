from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True 

driver = webdriver.Chrome(options=options)

url = "https://www.bing.com/search?q=pikachu&form=QBLH&sp=-1&lq=0&pq=pikachu&sc=12-7&qs=n&sk=&cvid=F4FDC17B1E63458CBF79D7A4C40C6C42&ghsh=0&ghacc=0&ghpl="

driver.get(url)

time.sleep(5)

html = driver.page_source

with open("bing_pikachu.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.quit()
print("HTML saved as 'bing_pikachu.html'")