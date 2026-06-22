# Define variables of various types
num_int = 10
num_float = 3.14
flag = True
text = "Python"

# f-String type conversion (to string automatically)
print("f-String Type Conversion:")
print(f"Integer as string: {num_int}")
print(f"Float as string: {num_float}")
print(f"Boolean as string: {flag}")
print(f"String itself: {text}")

# Confirm the type after conversion inside f-string (it's always str in output)
print("\nType confirmation in output:")
print(f"Type of {num_int} is {type(f'{num_int}')}")
print(f"Type of {num_float} is {type(f'{num_float}')}")
print(f"Type of {flag} is {type(f'{flag}')}")
print(f"Type of {text} is {type(f'{text}')}")