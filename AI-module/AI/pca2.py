graph = {
    "V1": {"V2": 10, "V3": 11},
    "V2": {"V1": 10, "V3": 8, "V5": 5},
    "V3": {"V1": 11, "V2": 8, "V4": 7, "V5": 12},
    "V4": {"V3": 7, "V5": 15},
    "V5": {"V2": 5, "V3": 12, "V4": 15}
}


def find_weight(u, v):
    if u in graph and v in graph[u]:
        print("Weight of edge", u, "-", v, "is:", graph[u][v])
    else:
        print("No direct edge between", u, "and", v)


def find_path(start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for vertex in graph[start]:
        if vertex not in path:
            new_path = find_path(vertex, end, path)
            if new_path:
                return new_path

    return None


def find_all_paths(start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []

    for vertex in graph[start]:
        if vertex not in path:
            new_paths = find_all_paths(vertex, end, path)
            for p in new_paths:
                paths.append(p)

    return paths


while True:
    print("\n--- Graph Operations ---")
    print("1. Find weight of edge between two vertices")
    print("2. Find one path between two vertices")
    print("3. Find all possible paths between two vertices")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        u = input("Enter first vertex: ").upper()
        v = input("Enter second vertex: ").upper()
        find_weight(u, v)

    elif choice == 2:
        start = input("Enter starting vertex: ").upper()
        end = input("Enter ending vertex: ").upper()

        path = find_path(start, end)

        if path:
            print("Path:", " -> ".join(path))
        else:
            print("No path found.")

    elif choice == 3:
        start = input("Enter starting vertex: ").upper()
        end = input("Enter ending vertex: ").upper()

        paths = find_all_paths(start, end)

        if paths:
            print("All possible paths:")
            for p in paths:
                print(" -> ".join(p))
        else:
            print("No path found.")

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")