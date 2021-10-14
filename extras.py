for i in range(0, 9):
    print(i)

#tuple
names = ("john doe", "jane doe")
print(names[1])
for name in names:
    print(name)

#names.append("jack doe")

def calculate_min_max(numbers):
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    return(min, max)

limits = calculate_min_max([10,6,78,16,86])
print(limits)

(a, b) = calculate_min_max([10,6,78,16,86])
print(a)

s = "indul a kutya aludni"
print(s.split(" "))

s = "sgaf, sdfs, hgjg"
for word in s.split(","):
    print(word)

names=["joe", "jack", "jane"]
print(",".join(names))

print(s.count("t"))

