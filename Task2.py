import requests

proxy = "http://techtaskuser:tech_task_pass68@104.164.125.82:20000"

r = requests.get('https://ipinfo.io/what-is-my-ip', proxies={"https": proxy})

with open("my_ip2.txt", "w") as file:
    file.write(r.text)

print("Response saved to 'my_ip2.txt'")