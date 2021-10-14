names = ["john doe", "jack doe", "jane doe"]
print(len(names))

print (names[1])

print(names[::-1])

fruits = ["orange"]
fruits += "apple"
print(fruits)

fruits = ["orange"]
fruits.append("apple")
print(fruits)

l = ["aaa", "bbbb"]
l += ["ccc"]
print(l)

fruits.insert (0, "alma")
print(fruits)

empty = []
print(empty)
empty += ["a"]
print(empty)

letters = []
letters += "john"
print(letters)

numbers = ["x", "y", "z"]
numbers[1] = "a"
print(numbers)

del (numbers[0])
print(numbers)

numbers.remove("z")
print(numbers)

print("x" in numbers)

print("a" in "jane doe")

while 'z' in numbers:
    numbers.remove("z")
print(numbers)

#összegzés
#egész számokat tartalmazó lista elemeit adjuk össze
numbers = [10, 24, 21, 25, 2, 234, 64, 234, 534]

sum = 0
for number in numbers:
    sum += number
print(sum)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i +=i

#szélsőérték-keresés
min =numbers [0]
for number in numbers:
    if number < min:
        min = number
print(min)

max =numbers [0]
for number in numbers:
    if number > max:
        max = number
print(max)

#van egy nevek listája, kikeresni belőle a leghosszabbat
names = ["john doe hosszunevu", "jack doe", "jane doe"]
hosszu = 0
for name in names:
    if len(name) > hosszu:
        hosszu = len (names)
print(hosszu)


