from bs4 import BeautifulSoup
from requests import get

content = get("https://index.hu").text
soup = BeautifulSoup(content, features="html.parser")
print(soup.get_text())

content = get("https://index.hu").text
soup = BeautifulSoup(content, features="html.parser")
only_text = soup.get_text()
lines = only_text.splitlines()
counters = {}
for line in lines:
    if len(line.strip()) != 0:
        print(line)
        words = line.split(" ")
        for word in words:
            transformed_word = word.strip().strip(".").strip(",").lower()
            if len(transformed_word) != 0:
                print(transformed_word)
                if transformed_word not in counters:
                    counters[transformed_word] = 1
                else:
                    counters[transformed_word] += 1
print(counters)

max_word = ""
max_count = 0
for word, counter in counters.items():
    if counter > max_count:
        max_word = word
        max_count = counter
print(max_word + " - " + str(max_count))
