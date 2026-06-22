import random
import math

def simulated_annealing(graph, heuristic, start, goal, temp=1000, cooling=0.95, min_temp=1):
    current = start
    path = [current]
    
    while current != goal and temp > min_temp:
        # Get current neighbors
        neighbors = graph[current]
        
        if not neighbors:
            break
        
        # Pick a random neighbor
        next_node = random.choice(neighbors)[0]
        current_h = heuristic[current]
        next_h = heuristic[next_node]
        
        # Calculate change in heuristic
        delta = next_h - current_h
        
        # Accept if better (lower heuristic) or sometimes accept worse
        if delta < 0:  # Better move
            current = next_node
            path.append(current)
        else:  # Worse move - accept with probability
            probability = math.exp(-delta / temp)
            if random.random() < probability:
                current = next_node
                path.append(current)
        
        # Cool down the temperature
        temp *= cooling
        
        # Prevent infinite loops
        if len(path) > 20:
            break
    
    if current == goal:
        return path
    else:
        print(f"Goal not reached. Ended at: {current}")
        return None

# Example
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 4), ('E', 1)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 4), ('G', 2)],
    'E': [('B', 1), ('G', 3)],
    'F': [('C', 5), ('G', 1)],
    'G': [('D', 2), ('E', 3), ('F', 1)]
}

heuristic = {'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 1, 'G': 0}

print("Simulated Annealing Search:")
path = simulated_annealing(graph, heuristic, 'A', 'G')
if path:
    print(f"Path: {' -> '.join(path)}")