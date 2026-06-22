# Find the sum of all even natural numbers between 1 to N

N = int(input("Enter the value of N: "))
total = 0

for i in range(2, N + 1, 2):
    total += i

print(f"The sum of all even natural numbers between 1 and {N} is {total}")