# 2) ინტეჯერი და შემოწმება

num = 12

if num > 10:
    print("more than 10")
else:
    print("less than 10")



# 3) მომხმარებლის რიცხვი

num = int(input("შეიყვანე რიცხვი: "))

if num == 15:
    print("equal to 15")
else:
    print("not equal to 15")



# 4) მომხმარებლის სტრინგი

text = input("შეიყვანე სტრინგი: ")

if text == "group84":
    print("you are correct")
else:
    print("you are wrong")



# 5) for ციკლი 50-დან 100-მდე, 5-ის გამოტოვებით

for i in range(50, 101, 5):
    print(i)



# 6) სახელი და გვარი for loop-ით

for i in range(1):
    print("Giorgi Giorgadze")



# 7) while loop 20-დან 50-მდე

i = 20
while i <= 50:
    print(i)
    i += 1



# 8) 0-დან 100-მდე ყველა რიცხვი

for i in range(101):
    print(i)

i = 0
while i <= 100:
    print(i)
    i += 1



# 9) 0-დან 100-ის ჩათვლით ყველა რიცხვი

for i in range(0, 101):
    print(i)

i = 0
while i <= 100:
    print(i)
    i += 1



# 10) 10-დან 20-მდე ყველა რიცხვი

for i in range(10, 21):
    print(i)

i = 10
while i <= 20:
    print(i)
    i += 1



# 11) 100-დან 200-მდე ყოველი მე-5 რიცხვი

for i in range(100, 201, 5):
    print(i)

i = 100
while i <= 200:
    print(i)
    i += 5



# 12) 10-დან 0-მდე

for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1



# 13) დადებითობა, უარყოფითობა, ნული

num = float(input("შეიყვანე რიცხვი: "))

if num > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif num < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")



# 14) ასაკის მიხედვით კატეგორიები

age = int(input("შეიყვანე ასაკი: "))

if age < 0:
    print("არასწორი ინფო")
elif age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")



# 15) სამი რიცხვის უდიდესი

n1 = float(input("რიცხვი 1: "))
n2 = float(input("რიცხვი 2: "))
n3 = float(input("რიცხვი 3: "))

max_num = max(n1, n2, n3)
print("უდიდესი რიცხვია:", max_num)

# 16) დღეების შემოწმება
day = int(input("შეიყვანე რიცხვი 1-დან 7-ის ჩათვლით: "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")



# 17) რიცხვის შემოწმება
num = float(input("შეიყვანე რიცხვი: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2)



# 18) პაროლის შემოწმება
password = input("შეიყვანე პაროლი: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")



# 19) 1-დან მომხმარებლის რიცხვამდე ჯამი
n = int(input("შეიყვანე რიცხვი: "))

sum_total = 0
for i in range(1, n + 1):
    sum_total += i

print("ჯამი:", sum_total)




