#van egy nevek listája, kikeresni belőle a leghosszabbat
names = ["john doe hosszunevu", "jack doe", "jane doe"]
# hosszu = 0
# for name in names:
#     if len(name) > hosszu:
#         hosszu = len (names)
# print(hosszu)

nax_name = names[0]
for name in names:
    if len(name) > len(nax_name):
        max_name =  name
print(nax_name)

numbers= [11, 24, 26, 44]
s = 0
for c in numbers:
    if c % 2 == 0:
        s +=1
print(s)

#eldöntés
names = ["john doe hosszunevu", "jack doe", "jane doe"]
for name in names:
    if name == "jack doe":
        print("van jack")
        break

#szűrés
numbers= [11, 24, 26, 44]
paros = []
for e in numbers:
    if e % 2 == 0:
        paros.append(e)
print(paros)

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(numbers)
print(even_numbers)

#transzformáció
names = ["john doe hosszunevu", "jack doe", "jane doe"]
len_of_names = []
for name in names:
    len_of_names.append(len(name))
print(len_of_names)


from math import sqrt
number = 9
print(sqrt(number))

#random
from random import randint, randrange
print (randint(0, 10))
print (randrange(10, 100))

#feladat
# szamok = int(input("adj meg 5 szamot"))
# print("kapott szamok" , szamok)
# max = szamok [0]
# for nagy in szamok:
#     if szamok > max:
#         max = szamok
# print(szamok)

# szam1 = int(input("add meg az elso szamot"))
# szam2 = int(input("add meg a masodik szamot"))
# szam3 = int(input("add meg a masodik szamot"))
# print(szam1, szam2, szam3)

numbers = []
i = 0
while i < 5:
    number = int(input(f"Add meg a {i + 1}. számot!\n"))
    numbers.append(number)
    i += 1
# print(numbers)

result = "Kapott számok: "
i = 0
for number in numbers:
    result = result + str(number)
    if i != len(numbers) - 1:
        result = result + ", "
    i += 1
print(result)

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"Ebből a legnagyobb: {max}")

print("john doe")
print("30")
print ("developer")

def print_employee():
    print("john doe")
    print("30")
    print("developer")

print_employee()

def print_employee_details (name, position, age):
    print(f"""
Alkalmazott neve: {name}
pozi: {position}
kora: {age}
    """)

def print_info():
    name = "john doe"
    print(name)
    return name

employee = print_info()
print("függyvényen kívül: " + employee)

def append_chars(name):
    return "xxx" + name + "xxx"

employee = append_chars("john")
print(employee)
