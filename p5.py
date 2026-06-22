a = 5
b = 5
c = 10
d = [1, 2, 3]
e = [1, 2, 3]

print("a is b:", a is b)             # True (small ints are cached)
print("a is c:", a is c)             # False
print("d is e:", d is e)             # False (lists with same values, but different objects)
print("d == e:", d == e)             # True (values are equal)

# Demonstration: "is" and "is not" are NOT arithmetic operators!
try:
    result = a is b + c
except Exception as error:
    print("a is b + c gives error:", error)
    
try:
    result = a is not c - b
except Exception as error:
    print("a is not c - b gives error:", error)

# Correct arithmetic operators should be used:
print("a + b =", a + b)
print("c - a =", c - a)
