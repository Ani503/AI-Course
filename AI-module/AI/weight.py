edges = []

n = int(input("Enter number of edges: "))

for i in range(n):
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")
    w = int(input("Enter weight: "))

    edges.append([u, v, w])

a = input("\nEnter first vertex to check: ")
b = input("Enter second vertex to check: ")

found = False

for edge in edges:
    if edge[0] == a and edge[1] == b:
        print("Edge exists between", a, "and", b)
        print("Weight =", edge[2])
        found = True

if found == False:
    print("No edge exists between", a, "and", b)