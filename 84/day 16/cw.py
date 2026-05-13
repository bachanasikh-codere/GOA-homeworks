# 1) for loop
# for loop არის ციკლი, რომელიც გამოიყენება მაშინ,
# როცა გვინდა რაიმე მოქმედება რამდენჯერმე გავიმეოროთ.
# იგი მუშაობს თანმიმდევრობით და გვაძლევს საშუალებას გადავუაროთ
# ელემენტებს ან რიცხვების დიაპაზონს.

# მაგალითი:
for i in range(5):
    print(i)



# 2) indentation
# indentation არის კოდის შეწევა (space ან tab),
# რომელიც Python-ში აუცილებელია, რათა ვიცოდეთ
# რომელი კოდი ეკუთვნის რომელ ბლოკს (მაგ: for, if).
# indentation გარეშე Python შეცდომას დააბრუნებს.



# 3) 0-დან 67-მდე

for i in range(0, 68):
    print(i)



# 4) 12-დან 87-მდე

for i in range(12, 88):
    print(i)



# 5) 4-დან 98-მდე, 2 ნაბიჯით

for i in range(4, 99, 2):
    print(i)



# 6) თქვენი სახელი 10-ჯერ

for i in range(10):
    print("Giorgi")



# 7) სიტყვის თითოეული ასო

word = input("შეიყვანე სიტყვა: ")

for letter in word:
    print(letter)



# 8) მომხმარებლის რიცხვი range-ში

num = int(input("შეიყვანე რიცხვი: "))

for i in range(num):
    print(i)
