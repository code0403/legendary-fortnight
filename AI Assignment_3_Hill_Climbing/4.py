import random

class PuzzleState:
    def __init__(self, state):
        self.state = state
        self.size = len(state)
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 'B':
                    return (i, j)

    def move_blank(self, direction):
        x, y = self.blank_pos
        new_x, new_y = x, y
        if direction == 'up' and x > 0:
            new_x -= 1
        elif direction == 'down' and x < self.size - 1:
            new_x += 1
        elif direction == 'left' and y > 0:
            new_y -= 1
        elif direction == 'right' and y < self.size - 1:
            new_y += 1
        else:
            return None  # Invalid move
        # Swap blank with the tile in the new position
        new_state = [row[:] for row in self.state]  # Create a deep copy
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return PuzzleState(new_state)

    def objective_function_O1(self, goal_state):
        """
        Objective function O1: Number of tiles displaced from their destined position.
        """
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] != goal_state.state[i][j] and self.state[i][j] != 'B':
                    count += 1
        return count

    def objective_function_O2(self, goal_state):
        """
        Objective function O2: Sum of the Manhattan distance of each tile from the goal position.
        """
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] != 'B':
                    tile = self.state[i][j]
                    x_goal, y_goal = goal_positions[tile]
                    distance += abs(i - x_goal) + abs(j - y_goal)
        return distance

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.state])

# Example usage:
initial_state = [
    ['T6', 'T7', 'T3'],
    ['T8', 'T4', 'T2'],
    ['T1', 'B', 'T5']
]
goal_state = [
    ['T1', 'T2', 'T3'],
    ['T4', 'T5', 'T6'],
    ['T7', 'T8', 'B']
]

# Dictionary to store the goal positions of each tile for O2
goal_positions = {}
for i in range(len(goal_state)):
    for j in range(len(goal_state)):
        goal_positions[goal_state[i][j]] = (i, j)

# Inside the PuzzleSolver class
class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def hill_climbing(self):
        current_state = self.initial_state
        explored_states = [current_state]
        while True:
            # Evaluate current state
            current_value = current_state.objective_function_O1(self.goal_state)

            # Check if current state is the goal state
            if current_state == self.goal_state:
                return "Success", current_state, len(explored_states), explored_states

            # Generate neighboring states by moving the blank tile
            neighbors = []
            for direction in ['up', 'down', 'left', 'right']:
                neighbor = current_state.move_blank(direction)
                if neighbor is not None:
                    neighbors.append(neighbor)

            # Choose the neighbor with the best objective function value
            best_neighbor = min(neighbors, key=lambda x: x.objective_function_O1(self.goal_state))
            best_value = best_neighbor.objective_function_O1(self.goal_state)

            # Check if the best neighbor has a better value
            if best_value >= current_value:
                # Local optimum reached, return current state
                return "Failure", current_state, len(explored_states), explored_states

            # Move to the best neighbor
            current_state = best_neighbor
            explored_states.append(current_state)

# Function to generate a random initial state for the puzzle
def generate_random_initial_state():
    tiles = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'B']
    random.shuffle(tiles)
    state = [tiles[i:i+3] for i in range(0, 9, 3)]
    return PuzzleState(state)

# Test the algorithm with different initial states
goal_puzzle = PuzzleState(goal_state)
for i in range(100):  # Try 100 times
    initial_state = generate_random_initial_state()
    solver = PuzzleSolver(initial_state, goal_puzzle)
    result, final_state, total_explored, explored_path = solver.hill_climbing()
    if result == "Success":
        print("Success Message:", result)
        print("Start State:")
        print(initial_state)
        print("Goal State:")
        print(goal_puzzle)
        print("Total number of states explored:", total_explored)
        print("List of states explored Path:")
        for state in explored_path:
            print(state)
        break
else:
    print("Failure Message: Unable to reach the goal state after 100 iterations")
    print("Start State:")
    print(initial_state)
    print("Goal State:")
    print(goal_puzzle)
    print("Total number of states explored before termination:", total_explored)
