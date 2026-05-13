# 2) რა არის boolean მონაცემთა ტიპი?
# Boolean არის მონაცემთა ტიპი, რომელსაც აქვს მხოლოდ ორი მნიშვნელობა:
# True (ჭეშმარიტი) და False (მცდარი)
# ვიყენებთ შედარებების დროს, მაგალითად:
# 5 > 3 -> True
# 2 > 10 -> False

# 3) რა არის binary code?
# Binary code არის სისტემა, რომელიც იყენებს მხოლოდ 0 და 1-ს
# 1 ნიშნავს ჩართულს (True), 0 ნიშნავს გამორთულს (False)
# კომპიუტერი ყველა ინფორმაციას ამ ფორმით ამუშავებს

# 4) რა არის bool() ფუნქცია?
# bool() ფუნქცია აბრუნებს True ან False-ს
# მაგალითად:
# bool(1) -> True
# bool(0) -> False
# bool("") -> False
# bool("hello") -> True

# 5)
a = 5
b = 10
print(a == b)

# 6)
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

if num1 > num2:
    print("პირველი რიცხვი მეტია")
elif num2 > num1:
    print("მეორე რიცხვი მეტია")
else:
    print("ორივე ტოლია")

# 7)
word = input("შეიყვანე სიტყვა: ")

if word == "Python":
    print("სწორია")
else:
    print("არ ემთხვევა")

# 8)
number = int(input("შეიყვანე რიცხვი: "))

if number > 100:
    print("100-ზე მეტია")
else:
    print("100-ზე ნაკლები ან ტოლია")

# 9)
password = input("შეიყვანე პაროლი: ")

if password == "Python123":
    print("სწორი პაროლი")
else:
    print("არასწორი პაროლი")

# 10)
a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))

print(a > b)
print(a < b)
print(a == b)

# 11)
s1 = input("შეიყვანე სიტყვა 1: ")
s2 = input("შეიყვანე სიტყვა 2: ")
s3 = input("შეიყვანე სიტყვა 3: ")
s4 = input("შეიყვანე სიტყვა 4: ")
s5 = input("შეიყვანე სიტყვა 5: ")

print(s1 + s2 + s3 + s4 + s5)

# 12)
n1 = float(input("რიცხვი 1: "))
n2 = float(input("რიცხვი 2: "))
n3 = float(input("რიცხვი 3: "))
n4 = float(input("რიცხვი 4: "))

average = (n1 + n2 + n3 + n4) / 4
print("საშუალო:", average)

# 13)
x = 10
y = 3.14
z = "Hello"
w = True

print(type(x))
print(type(y))
print(type(z))
print(type(w))

# 14)
str1 = "hello"
str2 = "hello"

print(str1 == str2)

# 15)
a = "10"
b = "20"
c = "30"
d = "40"

sum_numbers = int(a) + int(b) + int(c) + int(d)
print(sum_numbers)

# 16)
a = 30
b = 40
c = 50

result = str(a) + str(b) + str(c)
print(result)  