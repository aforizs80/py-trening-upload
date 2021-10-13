# i=1
# while i<=20:
# print(i * 7)
# i+=1
#

a, b = 1, 1
while (b <= 20):
    a, b = b * 7, b + 1
    if (a % 3 == 0):
        print(a, "*")
    else:
        print(a)

euro = 1
dollar = 1.65
while (euro < 16384):
    print(euro, "=", euro * dollar, "dollar")
    euro *=2


