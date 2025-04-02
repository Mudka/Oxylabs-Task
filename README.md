# Web Scraper Tasks


## Task 1: Get IP Address

```python
import requests

r = requests.get('https://ipinfo.io/what-is-my-ip')

with open("my_ip.txt", "w") as file:
    file.write(r.text)

print("Response saved to 'my_ip.txt'")
```

## Task 2: Get IP Address with Proxy
```python
## Task 1: Get IP Address Without Proxy

import requests

proxy = "http://techtaskuser:tech_task_pass68@104.164.125.82:20000"

r = requests.get('https://ipinfo.io/what-is-my-ip', proxies={"https": proxy})

with open("my_ip2.txt", "w") as file:
    file.write(r.text)

print("Response saved to 'my_ip2.txt'")
```

## Task 3: Scrape Bing Search Page
```python
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
```

## Task 3: Scrape 100 pages from Amazon
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")  
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
```
