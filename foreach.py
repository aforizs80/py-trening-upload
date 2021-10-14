name="john doe"

for c in name:
    if c == " ":
        break
    print(c)
print ("end")

szoveg = "hany e betu van ebben a mondatban"
print("e betuk a szovegben:", szoveg.count('e'))

szoveg = "hany e betu van ebben a mondatban"
if szoveg.count('e') > 0:
    print("van e betu a szovegben:")

name ="jane doe"
for a_char in name:
    if a_char == "e":
        print("talaltam e betut")

name ="jane doe"
for a_char in name:
    if a_char == "e" or a_char == "E":
        print("talaltam e betut")
        break

counter = 0
for a_char in name:
    if a_char == "e" or a_char =="E":
        counter +=1
print (counter)

result =""
counter = 0
for a_char in name:
    result += a_char
    if counter < len(name) - 1:
        result +=", "
    counter += 1
print (result)
result = result[:-1]

result = ""
for a_char in name:
    result = a_char + result
print(result)

name ="jane doe"
print(name == name [::-1])
print(name == result)

