# 1) მთელი რიცხვების სია, ყველა ელემენტი და ჯამი
numbers = [3, 5, 7, 2, 8, 10, 1]

# 1.1 დაბეჭდეთ ყველა ელემენტი
for num in numbers:
    print(num)

# 1.2 იპოვეთ სიის ელემენტების ჯამი
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print("Sum:", sum_numbers)


# 2) ლუწი რიცხვების დათვლა
numbers = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Number of even numbers:", even_count)


# 3) უმცირესი და უდიდესი ელემენტი
numbers = [12, 5, 20, 3, 8]
min_num = numbers[0]
max_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print("Min:", min_num)
print("Max:", max_num)


# 4) მხოლოდ კენტი რიცხვები
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num % 2 != 0:
        print(num)


# 5) მომხმარებლის რიცხვები მანამ სანამ 0 არ იქნება
sum_input = 0
while True:
    n = int(input("შეიყვანე რიცხვი (0 დასასრული): "))
    if n == 0:
        break
    sum_input += n
print("ჯამი:", sum_input)


# 6) მომხმარებლის რიცხვები მანამ სანამ უარყოფითი არ იქნება
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n < 0:
        break
    print("Positive number entered:", n)


# 7) მომხმარებლის რიცხვები მანამ სანამ რიცხვი იყოფა 5-ზე
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n % 5 == 0:
        print("Number divisible by 5:", n)
        break


# 8) მომხმარებლის რიცხვები მანამ სანამ ლუწი არ იქნება
attempts = 0
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    attempts += 1
    if n % 2 == 0:
        print("Even number entered:", n)
        break
print("Attempts needed:", attempts)


# 9) მომხმარებლის რიცხვები მანამ სანამ კენტი არ იქნება
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n % 2 != 0:
        print("Odd number entered:", n)
        break


# 10) continue და break მაგალითი
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n < 0:
        continue
    if n == 0:
        break
    print("Number entered:", n)


# 11) მომხმარებლის რიცხვები სანამ 100 არ იქნება, უარყოფითებს იგნორირება
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n == 100:
        break
    if n < 0:
        continue
    print("Accepted number:", n)
