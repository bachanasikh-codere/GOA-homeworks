# Instructions:
#  Given two boolean values a and b, store the result of a and b in result.
# Test Cases:
#  assert result == True when a = True, b = True
#  assert result == False when a = True, b = False
b=12
a=34
if b > a :
    print( str(b) + " მეტია " + str(a) + "-ზე")
elif  b == a :
    print( str(b) + " ტოლია " + str(a))
else:
    print( str(a) + " მეტია " + str(b) + "-ზე")