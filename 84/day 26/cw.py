# 1) სია integer ელემენტებით, ჯამი და საშუალო

numbers = [5, 10, 15, 20, 25]

# ჯამი
total = 0
for num in numbers:
    total += num
print("Sum:", total)

# საშუალო არითმეტიკული
average = total / len(numbers)
print("Average:", average)


# 2) მომხმარებლისგან რიცხვი სანამ არ შეიყვანს ჩაფიქრებულ რიცხვს
secret_number = 7

while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n == secret_number:
        print("Correct! Secret number entered.")
        break
    else:
        print("Wrong number, try again.")


# 3) მომხმარებლისგან რიცხვი სანამ არ შეიყვანს ლუწ რიცხვს
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n % 2 == 0:
        print("Even number entered:", n)
        break
    else:
        print("Odd number, try again.")
