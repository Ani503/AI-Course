N = int(input("Enter the value of N: "))
total = 0

for i in range(1, N + 1, 2):
    total += i

print(f"The sum of all odd numbers between 1 and {N} is {total}")