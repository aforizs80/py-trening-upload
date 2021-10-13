a = "étel"
if a is not None:
    print("tényleg alma")

i =0
while i < 7:
    print("het")
    i = i+1
print("end")

a, b, c = 1, 1, 1
while c < 11:
    print(b)
    a, b, c =b, a + b, c + 1
