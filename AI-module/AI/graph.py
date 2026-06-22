graph = {}

choice = input("Enter graph type (D for Directed, U for Undirected): ")

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)

    if choice == "U" or choice == "u":
        graph[v].append(u)

print("\nGraph Representation:")

for vertex in graph:
    print(vertex, "->", graph[vertex])