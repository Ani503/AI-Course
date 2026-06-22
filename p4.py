# Different data types
a = 10           # integer
b = 3.14         # float
c = "Hello"      # string
d = True         # boolean
e = [1, 2, 3]    # list
f = (4, 5, 6)    # tuple
g = {'x': 1, 'y': 2} # dictionary
h = {7, 8, 9}    # set
i = None         # NoneType

# Print the variable and its type
variables = [a, b, c, d, e, f, g, h, i]

for var in variables:
    print(f"Value: {var}, Type: {type(var)}")
