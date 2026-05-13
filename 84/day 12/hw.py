# 1) კომენტარების სახით ჩამოთვალეთ ყველა შედარებითი ოპერატორი
# >   - მეტობა
# <   - ნაკლებობა
# >=  - მეტია ან ტოლია
# <=  - ნაკლებია ან ტოლია
# ==  - ტოლობა
# !=  - არ უდრის

# > მაგალითები
print(10 > 5)
print(7 > 2)
print(3 > 9)
print(15 > 10)
print(1 > 8)

# < მაგალითები
print(2 < 5)
print(1 < 9)
print(10 < 3)
print(4 < 8)
print(7 < 6)

# >= მაგალითები
print(5 >= 5)
print(10 >= 7)
print(3 >= 8)
print(20 >= 20)
print(9 >= 2)

# <= მაგალითები
print(4 <= 4)
print(2 <= 7)
print(9 <= 3)
print(5 <= 10)
print(8 <= 8)

# == მაგალითები
print(5 == 5)
print(7 == 2)
print(10 == 10)
print(1 == 3)
print(6 == 6)

# != მაგალითები
print(5 != 3)
print(4 != 4)
print(10 != 2)
print(7 != 1)
print(9 != 9)



# 2) კომენტარების სახით ახსენით logical operators
# Logical operators გამოიყენება რამდენიმე პირობის ერთად შესამოწმებლად

# and - აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობა True არის
# or - აბრუნებს True-ს თუ ერთ-ერთი პირობა მაინც True არის
# not - ცვლის შედეგს
# True -> False
# False -> True



# 3) logical operator-ების მაგალითები

# and
print(5 > 2 and 10 > 3)
print(7 > 4 and 2 > 9)
print(1 < 5 and 3 < 8)

# or
print(5 > 10 or 7 > 3)
print(1 > 4 or 2 > 8)
print(6 < 9 or 10 < 3)

# not
print(not True)
print(not False)
print(not(5 > 2))



# 4) მომხმარებლის რიცხვის შედარება

my_number = 50

user_number = int(input("შეიყვანე რიცხვი: "))

print(user_number > my_number)



# 5) სახელის შემოწმება

my_name = "Nika"

user_name = input("შეიყვანე სახელი: ")

print(user_name == my_name)



# 6) ასაკის შემოწმება

age = int(input("შეიყვანე ასაკი: "))

print(age > 18)
