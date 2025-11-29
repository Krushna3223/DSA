from collections import deque

# Helper: Find possible moves from current state 
def get_neighbors(state):
    moves = []
    idx = state.index('0')           # Find blank position 
    row, col = divmod(idx, 3)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right 
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            moves.append(''.join(new_state))
    return moves

def bfs(start, goal):
    queue = deque([(start, [start])])  # (state, path) 
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Changed input values only
start = "125340678"   # new initial configuration
goal  = "123456780"   # same goal (standard)
solution = bfs(start, goal)

if solution:
    print("Steps to solve the 8-Puzzle Problem:")
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found.")
