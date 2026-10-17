def two_oldest_ages(ages):
    oldest = max(ages)
    ages.remove(oldest)
    return [max(ages), oldest]



def solution(string):
    result = ""
    for i in string:
        result = i + result
    return result

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
