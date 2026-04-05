# def r(n):
#     s = 0
#     while n > 0:
#         d = n % 10 
#         n = n // 10         
#         s = s * 10 + d
                    
#     return s
# x = int(input("დაწერე რაიმsე რიცხვი "))

# print(r(x))


#  # ჯერ დავატრიალებ ციკლს იქამდე სანამ ბ არ დამრთავდება შემდეგ ა-ს  ა-ს ბ-ე რაოდენობის და მერე დავპრინტო


# a = int( input("დაწერე რაიმე რიცხვი:") )
# b = int( input("კიდე დაწერე რაიმე რიცხვი:") )


# c = 0
# for i in range (0, b) :
#     c = c + a
# print(c)


# n = int(input("შემოიტანე მასივის სიგრძე: "))
# b = [] 
# for i in range (0, n) :
#     b.append(int(input("შემოიტანე მასივის " + str(i) + "  ელემენტი: ")))
 
# for i in range (n - 1, -1, -1) :
#     print(b[i])

a = int(input("დაწერე რაიმე რიცხვი"))
b = 0
while a > 0 :
    a = a // 10
    b = b + 1
print(b)
