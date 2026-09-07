# 1
def odd_even(arr):
    if sum(arr)% 2 == 0:
        return "even"
    else :
        return "odd"




# 2
def no_space(x):
    result = ""

    for i in x:
        if i != " ":
            result += i

    return result

# 3
def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False