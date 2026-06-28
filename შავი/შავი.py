# def r(n):
#     s = 0
#     while n > 0:
#         d = n % 10 
#         n = n // 10         
#         s = s * 10 + d
                    
#     return s
# x = int(input("დაწერე რაიმე რიცხვი "))

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

# a = int(input("დაწერე რაიმე რიცხვი"))
# b = 0
# while a > 0 :
#     a = a // 10
#     b = b + 1
# print(b)

# n = int(input("შემოიტანე მასივის სიგრძე: "))
# a = [] 
# for i in range (0, n) :
#     a.append(int(input("შემოიტანე მასივის " + str(i) + "  ელემენტი: "))) 

# number=0
# for i in a :
#     number = number * 10 + i   
# print(number)
 

# # N = 3
# #   A = [5,  6,  5]
# #   B = [4,  4,  7]
# # ----------------------
# #  SUM=  10   1  2
# #  SUM 2 
 


# #  C=12




# n = int(input("შემოიტანე მასივის სიგრძე : ")) 
# a = []
# b = []
# for i in range (  1, n + 1) :
#     a.append(int(input("შემოიტანე A მასივის " + str(i) + " ელემენტი,  ციფრების სახით: "))) 
# for i in range (1, n + 1) :
#    b.append(int(input("შემოიტანე B მასივის " + str(i) + " ელემენტი,  ციფრების სახით: ")))

# sum = ""

# d = 0
# for i in range (n - 1, -1, -1 ) :
#     c = a[i] + b[i] +  d
#     if c > 9 :
#         sum = str(c % 10) + sum 
#         d = c // 10
#     else : 
#         sum = str(c) + sum 

# if d > 0 : 
#     sum =  str(d) + sum 
       
# print(sum)


 



# n = int(input("შემოიტანეთ მასივის სიგრძე :")) 
# a=[]
# b=[]

# for i in range (  1, n + 1) :
#     a.append(int(input("შემოიტანე A მასივის " + str(i) + " ელემენტი,  ციფრების სახით: "))) 
# for i in range (1, n + 1) :
#    b.append(int(input("შემოიტანე B მასივის " + str(i) + " ელემენტი,  ციფრების სახით: ")))

# sum = ""

# d = 0
# for i in range (n - 1, -1, -1 ) :
#     c = a[i] - b[i] -  d
#     if c > 9 :
#         sum = str(c * 10) + sum 
#         d = c ** 10
#     else : 
#         sum = str(c) + sum 

# if d < 0 : 
#     sum =  str(d) - sum 
       
# print(sum)




# n = int(input("შემოიტანეთ მასივის სიგრძე :"))
# a=[]

# a.append(int(input("შემოიტანე A მასივის " + " ელემენტი,  ციფრების სახით: ")))
# b = max(a)
# for i in range(n) :
#     if b == n :
#         print(b) and print(n)
