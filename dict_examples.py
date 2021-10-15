products = {"orange": 30, "apple": 50, "bread": 10}
print(products["orange"])

products["orange"] = 29
print(products)

products["milk"] = 16
print(products)

my_products = {}
print(my_products)
my_products["bread"] = 88
print(my_products)

del(products["orange"])
print(products)

#products.clear()
print(products)

print(products.keys())

for key in products.keys():
    print(key + ": " + str(products[key]))

for value in products.values():
    print(value)

#print("orange" in products):

if "orange" in products:
    print("narancs benne van")

for item in products.items():
    print(item[0] + " " + str(item[1]))

for (key, value) in products.items():
    print(key + " " + str(value))

employee = {
    "name": "john doe",
    "age": 30,
    "salary": 100_000,
    "address": {
        "city": "Budapest",
        "stree": "petofi",
        "hazszam": 10
    }
}
print(employee["name"])
print(employee["salary"])

john = {
    "name": "john doe",
    "age": 30,
    "salary": 100_000,
    "address": {
        "city": "Budapest",
        "street": "petofi",
        "hazszam": 10
    },
    "skills": ["java", "python", "javascript"]
}

print(john["address"]["city"])

jack = {
    "name": "jack",
    "age": 40,
    "salary": 200_000
}

print(john["name"])
print(john["salary"])

employees = [
    {"name": "john"},
    {"name":"jack"}
]

print(employees[1]["name"])
