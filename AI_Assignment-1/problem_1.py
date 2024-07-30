import random
from collections import deque

# Function to generate a random 3x3 grid
def generate_random_grid():
    numbers = list(range(1, 9))
    random.shuffle(numbers)
    numbers.append('B')
    return [numbers[i:i+3] for i in range(0, 9, 3)]

# Function to check if the target state is reachable from a given state
def is_reachable(initial_state, target_state, search_algorithm):
    if search_algorithm == 'BFS':
        return bfs(initial_state, target_state)
    elif search_algorithm == 'DFS':
        return dfs(initial_state, target_state)

# Breadth-First Search (BFS) method
def bfs(initial_state, target_state):
    visited = set()
    queue = deque([(initial_state, [])])  # Queue of (state, path) tuples

    while queue:
        state, path = queue.popleft()
        if state == target_state:
            return True, path
        visited.add(str(state))
        for move in find_moves(state):
            new_state = move_blank(state, move)
            if str(new_state) not in visited:
                queue.append((new_state, path + [move]))

    return False, None  # No solution found

# Depth-First Search (DFS) method
def dfs(initial_state, target_state, depth_limit=20):  # Adjust depth limit as needed
    visited = set()
    stack = [(initial_state, [])]  # Stack of (state, path) tuples

    while stack:
        state, path = stack.pop()
        if state == target_state:
            return True, path
        visited.add(str(state))
        if len(path) < depth_limit:  # Limit the depth to avoid infinite loops
            for move in find_moves(state):
                new_state = move_blank(state, move)
                if str(new_state) not in visited:
                    stack.append((new_state, path + [move]))

    return False, None  # No solution found

# Function to find all possible moves from a given state
def find_moves(state):
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    
    # Find the position of the blank space ('B')
    for i in range(3):
        for j in range(3):
            if state[i][j] == 'B':
                row, col = i, j
                
    # Generate all possible moves
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]  # Make a copy of the current state
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]  # Swap blank space with adjacent cell
            moves.append(new_state)
            
    return moves

# Function to move the blank space in the board
def move_blank(board, move):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'B':
                blank_row = i
                blank_col = j
                break
    # Move the blank space
    if move == 'up':
        board[blank_row][blank_col] = board[blank_row - 1][blank_col]
        board[blank_row - 1][blank_col] = 'B'
    elif move == 'down':
        board[blank_row][blank_col] = board[blank_row + 1][blank_col]
        board[blank_row + 1][blank_col] = 'B'
    elif move == 'left':
        board[blank_row][blank_col] = board[blank_row][blank_col - 1]
        board[blank_row][blank_col - 1] = 'B'
    elif move == 'right':
        board[blank_row][blank_col] = board[blank_row][blank_col + 1]
        board[blank_row][blank_col + 1] = 'B'

    return board

# Print the path to solve the puzzle
def print_solution(path):
    if path is not None:
        for i, move in enumerate(path):
            print(f"Step {i + 1}: Move {move}")
    else:
        print("No solution found.")


# Main function
if __name__ == '__main__':
    # Generate random initial and target states
    initial_state = generate_random_grid()
    target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]

    print("Initial State:")
    for row in initial_state:
        print(' '.join(map(str, row)))
    print("Target State:")
    for row in target_state:
        print(' '.join(map(str, row)))

    # Perform BFS and print solution
    bfs_reachable, bfs_path = is_reachable(initial_state, target_state, 'BFS')
    print("\nBFS Solution:")
    if bfs_reachable:
        print_solution(bfs_path)
    else:
        print("Target state is not reachable.")

    # Perform DFS and print solution
    dfs_reachable, dfs_path = is_reachable(initial_state, target_state, 'DFS')
    print("\nDFS Solution:")
    if dfs_reachable:
        print_solution(dfs_path)
    else:
        print("Target state is not reachable.")
