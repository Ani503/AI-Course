def hill_climbing(graph, heuristic, start, goal):
    current = start
    path = [current]
    
    while current != goal:
        neighbors = graph[current]
        
        # Find the neighbor with best (lowest) heuristic value
        best_neighbor = None
        best_heuristic = float('inf')
        
        for neighbor, cost in neighbors:
            if heuristic[neighbor] < best_heuristic:
                best_heuristic = heuristic[neighbor]
                best_neighbor = neighbor
        
        # If no better neighbor found, stuck at local maximum
        if best_heuristic >= heuristic[current]:
            print(f"Stuck at local optimum: {current}")
            return None
        
        # Move to the best neighbor
        current = best_neighbor
        path.append(current)
    
    return path

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

path = hill_climbing(graph, heuristic, 'A', 'G')
if path:
    print(f"Path: {' -> '.join(path)}")