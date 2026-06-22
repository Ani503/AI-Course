graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    a = input("Enter first vertex: ")
    b = input("Enter second vertex: ")

    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

start = input("Enter starting vertex: ")
goal = input("Enter goal vertex: ")


def dls(node, goal, limit, path):
    path.append(node)

    if node == goal:
        return path

    if limit == 0:
        path.pop()
        return None

    for child in graph[node]:
        if child not in path:
            result = dls(child, goal, limit - 1, path)

            if result:
                return result

    path.pop()
    return None


limit = int(input("\nEnter depth limit for DLS: "))

answer = dls(start, goal, limit, [])

print("\nDLS Result:")

if answer:
    print("Path found:", answer)
else:
    print("Path not found")


print("\nID Search Result:")

max_depth = int(input("Enter maximum depth for ID Search: "))

found = False

for depth in range(max_depth + 1):
    answer = dls(start, goal, depth, [])

    if answer:
        print("Path found at depth", depth)
        print("Path:", answer)
        found = True
        break

if found == False:
    print("Path not found")