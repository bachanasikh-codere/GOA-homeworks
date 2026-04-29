    #1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

    #2
def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
    #3
def double_char(s):
    result = ""
    for c in s:
        result += c * 2
    return result
    #4
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)
    #5
def is_even(n): 
    return n % 2 == 0












