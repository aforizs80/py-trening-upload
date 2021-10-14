# i = 1
# while i<=20:
#     print (i * 7)
#     i = i + 1
#
# eur = 1
# exchange_rate = 1.65
# while eur < 16385:
#     print(eur, "euro=", eur * exchange_rate, "dollar")
#     eur *=2
#
#
# for i in range (1,8):
#     print(i*"*")

# i=1
# while i<=20:
#     result=i * 7
#     if result % 3 == 0:
#         print(str(result) + " *")
#     else:
#         print(str(result))
# i = i + 1
#
# stars = 1
# while stars < 7:
# #    print("*" * stars)
#     line = ""
#     number = 0
#     while number < stars:
#         line+="*"
#         number+=1
#     print(line)
#     stars = stars + 1

# name = "joe"
# print(len(name))
# print(name[3])

# lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
#  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
#  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
#   esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
#   sunt in culpa qui officia deserunt mollit anim id est laborum."""
# print(lorem)
#
# print(name[666])

name = "joe"
length = len(name)
i = 0
while (i <length):
    print (name[i])
    i=i + 1

for c in name:
    if c == " ":
    print(c)

name ="joe"
age = 35

print ("a", name, "alkalmazott", age, "éves")
print ("a" + name + "alkalmazott" + str(age)+ "áves!")

print(f"a {name} alkalmazott {age} éves")

name="John Doe"
print(name[1:6])

name="John Doe"
print(name[1:6:2])
print(name[::-1])

