# Check whether a given number is a strong number or not
# (sum of factorial of digits = number)

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    # Calculate factorial of the digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_fact += fact
    temp //= 10

if sum_fact == num:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")