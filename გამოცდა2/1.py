# Ask the user to enter their weight in kilograms and height in meters using input().
# Calculate the Body Mass Index (BMI) using the given formula.
 
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print the result
print("Your BMI is:", bmi)
ა=123
ბ=34
for i in range(ა>ბ):
    print() 


























































    lst = [1, 2, 5, 7]
result = 5 in lst
print(result)
#Instructions:Ask the user to input their name, surname, age, place of living, and gender.Store the inputs in appropriate variables and display the information in the terminal in the following format:"your name is {name} your age is {age} u living in {living} your gender is {gender}"Expected Output:The sentence should correctly include the user’s provided name, age, place of living, and gender.



name = input( "what is your name: ")
surname = input("what is your surname: ")
age = input("how old are you:")
place = input("where do you live: ")
gender = input("what gender are you: ")


print(f" name is {name}surname is {surname} age is {age} u living in {place} your gender is {gender} ")
#Write a program reverse_string(s) that takes a string and returns its reverse. The function should:
 
word="abragi"

print(word[::-1])

word1="hidroeleqtrosadguri"
print(word1[::-1])
#Instructions:
#write code that returns True if number is even, otherwise False.
#Test Cases:
#assert is_even(4) == True
#assert is_even(7) == False
#assert is_even(0) == True

def is_even(number):
    return number % 2 == 0