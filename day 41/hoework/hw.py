def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())

def make_negative(number):
    if number > 0:
        return -number
    return number

print(make_negative(5))   # -5
print(make_negative(-7))  # -7
print(make_negative(0))   # 0


def fake_bin(x):
    return "".join("0" if int(i) < 5 else "1" for i in x)



def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())

def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())