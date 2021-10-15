from requests import get


response = get("https://www.training360.com/")
print(response.text)

lines = response.text.splitlines()
print(lines)

from requests import get
from datetime import datetime
response = get("https://index.hu")
lines = response.text.splitlines()
a = 0
for i in lines:
    if "koronavirus" in i.lower():
        a += 1
        with open("korona.txt", encoding="utf-8", mode="a") as f:
            f.write(f"Szam: {a} - {datetime.now()}\n")

