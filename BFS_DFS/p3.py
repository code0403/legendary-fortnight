import random
from collections import deque
import time

# Function to generate a random 3x3 grid
def generate_random_grid():
    numbers = list(range(1, 9))
    random.shuffle(numbers)
    numbers.append('B')
    return [numbers[i:i+3] for i in range(0, 9, 3)]

# Function to check if the target state is reachable from a given state
def is_reachable(initial_state, target_state, search_algorithm):
    start_time = time.time()  # Record start time
    if search_algorithm == 'BFS':
        result, depth = bfs(initial_state)  # Implement BFS
    elif search_algorithm == 'DFS':
        result, depth = dfs(initial_state)  # Implement DFS
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time  # Calculate time taken
    return result, depth, time_taken

# Function to perform Breadth-First Search (BFS)
def bfs(initial_state):
    target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]
    visited = set()
    queue = deque([(initial_state, 0)])  # Queue of (state, depth) tuples
    
    while queue:
        state, depth = queue.popleft()
        if state == target_state:
            return True, depth
        visited.add(str(state))
        for next_state in find_moves(state):
            if str(next_state) not in visited:
                queue.append((next_state, depth + 1))
    return False, -1  # Target state not reachable

# Function to perform Depth-First Search (DFS)
def dfs(initial_state):
    target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]
    visited = set()
    stack = [(initial_state, 0)]  # Stack of (state, depth) tuples
    
    while stack:
        state, depth = stack.pop()
        print("Current state:")
        for row in state:
            print(' '.join(map(str, row)))
        print("Depth:", depth)
        if state == target_state:
            return True, depth
        visited.add(str(state))
        for next_state in find_moves(state):
            if str(next_state) not in visited:
                stack.append((next_state, depth + 1))
    return False, -1  # Target state not reachable

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

# Main function to solve the problem
def solve_problem():
    target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]
    search_algorithms = ['BFS', 'DFS']
    
    while True:
        initial_state = generate_random_grid()
        print("Initial State:")
        for row in initial_state:
            print(' '.join(map(str, row)))
        print("Target State:")
        for row in target_state:
            print(' '.join(map(str, row)))
        
        for algorithm in search_algorithms:
            reachable, steps, time_taken = is_reachable(initial_state, target_state, algorithm)
            if reachable:
                print(f"{algorithm}: Target state is reachable in {steps} steps. Time taken: {time_taken:.6f} seconds.")
            else:
                print(f"{algorithm}: Target state is not reachable. Time taken: {time_taken:.6f} seconds.")

            if reachable:
                break  # If target state is reachable by any algorithm, stop retrying

        if reachable:
            break  # Exit loop if target state is reached


# Call the main function to solve the problem
solve_problem()
