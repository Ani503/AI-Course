# Simple calculator using nested functions

def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
    choice = input("Enter choice (1/2/3/4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(a, b)}")
    elif choice == '2':
        print(f"Result: {subtract(a, b)}")
    elif choice == '3':
        print(f"Result: {multiply(a, b)}")
    elif choice == '4':
        print(f"Result: {divide(a, b)}")
    else:
        print("Invalid input")

calculator()