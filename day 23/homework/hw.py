#1)

def solution(string):
    revert=""
    for i in range( len(string) - 1, -1, -1 ) :
        revert = revert + string[i]
    return revert

#2)

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#3)

def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

#4)

def repeat_str(repeat, string):
    return string * repeat

#5)

def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
