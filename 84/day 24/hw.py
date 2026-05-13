# 2) დადებითი, უარყოფითი ან ნული და ლუწი/კენტი შემოწმება
num = int(input("შეიყვანე რიცხვი: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 3) რიცხვების შეყვანა სანამ უარყოფითი არ იქნება
while True:
    n = int(input("შეიყვანე რიცხვი: "))
    if n < 0:
        print("Negative number entered, exiting loop.")
        break
    else:
        print("Positive number, continue.")


# 4) PIN კოდის შემოწმება 3 მცდელობით
correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("შეიყვანე PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    attempts += 1
else:
    print("Access Denied")


# 5) სია fruits და მესამე ელემენტი
fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])  



# 6) სია numbers და მეორე ელემენტის შეცვლა
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)  

# 7) ინდექსის გამოყენებით ელემენტის არჩევა
colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
index = int(input("შეიყვანე ინდექსი (0-დან 4): "))
print(colors[index])



# 8) სია animals და ბოლო ელემენტის შეცვლა
animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)



# 9) ინდექსის და ახალი ფერის გამოყენებით ცვლილება
colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("შეიყვანე ინდექსი (0-დან 3): "))
new_color = input("შეიყვანე ახალი ფერი: ")
colors[index] = new_color
print(colors)
