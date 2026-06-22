from itertools import permutations

n = int(input("Enter number of cities: "))

cost = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

start = 0
cities = list(range(1, n))

min_cost = 999999
best_path = []

for path in permutations(cities):
    total = 0
    current = start

    for city in path:
        total = total + cost[current][city]
        current = city

    total = total + cost[current][start]

    if total < min_cost:
        min_cost = total
        best_path = path

print("\nMinimum Cost:", min_cost)

print("Best Path:", end=" ")
print(start, end=" -> ")

for city in best_path:
    print(city, end=" -> ")

print(start)