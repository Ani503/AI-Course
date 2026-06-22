def a_star(graph, heuristic, start, goal):
    visited = set()
    queue = [(0 + heuristic[start], 0, start, [start])]  # (f_cost, g_cost, node, path)
    
    while queue:
        queue.sort()  # Sort by f_cost (smallest first)
        f, g, node, path = queue.pop(0)
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    new_g = g + cost  # Actual cost to reach neighbor
                    new_f = new_g + heuristic[neighbor]  # f = g + h
                    queue.append((new_f, new_g, neighbor, path + [neighbor]))

# Example
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 1, 'G': 0}

path = a_star(graph, heuristic, 'A', 'G')
print(f"Path: {' -> '.join(path)}")