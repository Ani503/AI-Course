def greedy_bfs(graph, heuristic, start, goal):
    visited = set()
    queue = [(heuristic[start], start, [start])]
    
    while queue:
        queue.sort()  # Sort by heuristic value
        h, node, path = queue.pop(0)
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    queue.append((heuristic[neighbor], neighbor, path + [neighbor]))

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

path = greedy_bfs(graph, heuristic, 'A', 'G')
print(f"Path: {' -> '.join(path)}")