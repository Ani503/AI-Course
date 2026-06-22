import math

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

a = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    a.append(row)

for i in range(e):
    s = int(input("Enter starting vertex: "))
    t = int(input("Enter ending vertex: "))

    a[s][t] = 1
    a[t][s] = 1

print("Adjacency Matrix:")

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()