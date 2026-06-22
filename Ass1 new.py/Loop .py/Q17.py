# Find the sum of first n natural numbers

n = int(input("Enter the value of n: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"The sum of first {n} natural numbers is {total}")
