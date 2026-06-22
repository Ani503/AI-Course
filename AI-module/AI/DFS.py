graph = {}

edges = int(input("Enter number of edges: "))
for i in range(edges):
    u = input(f"Edge {i + 1} - Enter first vertex: ")
    v = input(f"Edge {i + 1} - Enter second vertex: ")

    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting vertex for DFS: ")
visited = set()

print("\nGraph adjacency list:")
for vertex, neighbors in graph.items():
    print(vertex, "->", neighbors)

print("\nDFS traversal:", end=" ")

def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph.get(node, []):
            dfs(neighbor)

if start not in graph:
    print(f"{start} is not in the graph.")
else:
    dfs(start)
    print()