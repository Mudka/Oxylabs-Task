import requests

r = requests.get('https://ipinfo.io/what-is-my-ip')

with open("my_ip.txt", "w") as f:
    f.write(r.text)

print("Response saved to 'my_ip.txt'")