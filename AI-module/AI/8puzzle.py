from collections import deque

def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def next_states(state):
    moves = []
    blank = state.index(0)
    row, col = blank // 3, blank % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, c in directions:
        new_row = row + r
        new_col = col + c

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]

            moves.append(tuple(new_state))

    return moves
start = tuple(map(int, input("Enter start state using 0 for blank: ").split()))
goal = tuple(map(int, input("Enter goal state using 0 for blank: ").split()))
queue = deque()
queue.append((start, [start]))
visited = set()
visited.add(start)
found = False
while queue:
    state, path = queue.popleft()

    if state == goal:
        print("\nSolution found!")
        print("Number of moves:", len(path) - 1)

        for step in path:
            show(step)

        found = True
        break

    for new_state in next_states(state):
        if new_state not in visited:
            visited.add(new_state)
            queue.append((new_state, path + [new_state]))
if found == False:
    print("No solution found")