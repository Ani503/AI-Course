value = input("Enter something: ")

try:
    int_value = int(value)
    print(f"{value} is an integer.")
except ValueError:
    print(f"{value} is not an integer.")