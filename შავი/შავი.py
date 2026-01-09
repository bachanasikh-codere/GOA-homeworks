a = int(input("დაწერე რაიმე რიცხვი: "))
b = int(input(" კიდევ დაწერე რაიმე რიცხვი: "))
c = int(input(" კიდევ დაწერე რაიმე რიცხვი: "))
if a > b and a > c :
    print(a)
elif a == b == c :
    print(a)
    print(b)
    print(c)

elif c > b :
    print(c)

elif a == b :
    print(a)
    print(b)

elif a == c :
    print(a)
    print(c)

elif c == b :
    print(c)
    print(b)   


else :
    print(b)


