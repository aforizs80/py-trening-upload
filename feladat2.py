i = 1
while i<=20:
    print (i * 7)
    i = i + 1

eur = 1
exchange_rate = 1.65
while eur < 16385:
    print(eur, "euro=", eur * exchange_rate, "dollar")
    eur *=2


for i in range (1,8):
    print(i*"*")

# i=1
# while i<=20:
#     result=i * 7
#     if result % 3 == 0:
#         print(str(result) + " *")
#     else:
#         print(str(result))
# i = i + 1

stars = 1
while stars < 7:
#    print("*" * stars)
    line = ""
    number = 0
    while number < stars:
        line+="*"
        number+=1
    print(line)
    stars = stars + 1
