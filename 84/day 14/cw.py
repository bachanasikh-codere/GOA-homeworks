# 1) რა არის Flowchart?
# Flowchart არის დიაგრამა, რომელიც პროგრამის ნაბიჯებს
# და მოქმედებების თანმიმდევრობას აჩვენებს.
#
# მაგალითი:
# Start -> შეიყვანე რიცხვი -> დაბეჭდე რიცხვი -> End



# 2) რა არის Sequencing?
# Sequencing ნიშნავს, რომ კოდი სრულდება
# თანმიმდევრობით, ზემოდან ქვემოთ.

print("Hello")
print("World")
# ჯერ დაიბეჭდება Hello
# შემდეგ World



# 3) რა არის Iteration?
# Iteration ნიშნავს ერთი და იგივე მოქმედების
# რამდენჯერმე გამეორებას.

for i in range(3):
    print("Python")

# შედეგი:
# Python
# Python
# Python



# 4) რა არის Selection?
# Selection ნიშნავს არჩევანის გაკეთებას პირობის მიხედვით.
# გამოიყენება if / else.

age = 18

if age >= 18:
    print("სრულწლოვანი")
else:
    print("არასრულწლოვანი")
