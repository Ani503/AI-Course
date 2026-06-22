graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

start = input("Enter starting vertex: ")
end = input("Enter ending vertex: ")

queue = [[start]]
visited = []

found = False

while queue:
    path = queue.pop(0)
    vertex = path[-1]

    if vertex == end:
        print("Path found:", path)
        found = True
        break

    if vertex not in visited:
        visited.append(vertex)

        for neighbour in graph[vertex]:
            new_path = path + [neighbour]
            queue.append(new_path)

if found == False:
    print("No path found")