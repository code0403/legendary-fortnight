import random

class PuzzleState:
    def __init__(self, grid):
        self.grid = grid
        self.blank_position = self.find_blank_position()

    def find_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 'B':
                    return (i, j)
        return None

    def __eq__(self, other):
        return self.grid == other.grid

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])

class HillClimbing:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def objective_function1(self, state):
        # O1(n): Number of tiles displaced from their destined position
        displaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if state.grid[i][j] != self.goal_state.grid[i][j]:
                    displaced_tiles += 1
        return displaced_tiles

    def objective_function2(self, state):
        # O2(n): Sum of the Manhattan distance of each tile from the goal position
        distance = 0
        for i in range(3):
            for j in range(3):
                if state.grid[i][j] != 'B':
                    tile = int(state.grid[i][j])
                    goal_position = self.find_goal_position(tile)
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return distance

    def find_goal_position(self, tile):
        for i in range(3):
            for j in range(3):
                if self.goal_state.grid[i][j] == str(tile):
                    return (i, j)

    def generate_neighbours(self, state):
        neighbours = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        blank_i, blank_j = state.blank_position
        for di, dj in directions:
            new_i, new_j = blank_i + di, blank_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_grid = [row[:] for row in state.grid]
                new_grid[blank_i][blank_j], new_grid[new_i][new_j] = new_grid[new_i][new_j], new_grid[blank_i][blank_j]
                neighbours.append(PuzzleState(new_grid))
        return neighbours

    def hill_climbing_search(self, objective_function):
        current_state = self.initial_state
        current_value = objective_function(current_state)
        states_explored = 0
        max_iterations = 100
        
        while True:
            neighbours = self.generate_neighbours(current_state)
            next_best_state = None
            next_best_value = float('inf')

            for neighbour in neighbours:
                neighbour_value = objective_function(neighbour)
                states_explored += 1
                if neighbour_value < next_best_value:
                    next_best_state = neighbour
                    next_best_value = neighbour_value
            
            if next_best_value >= current_value or states_explored >= max_iterations:
                break
            
            current_state = next_best_state
            current_value = next_best_value
        
        return current_state, states_explored

def create_random_state():
    numbers = list(map(str, range(1, 9)))  # Convert integers to strings
    numbers.append('B')
    random.shuffle(numbers)
    return PuzzleState([numbers[:3], numbers[3:6], numbers[6:]])

def main():
    goal_state = PuzzleState([
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', 'B']
    ])
    
    for _ in range(100):
        initial_state = create_random_state()
        search_algorithm = HillClimbing(initial_state, goal_state)
        
        # Hill Climbing with Objective Function O1(n)
        final_state1, states_explored1 = search_algorithm.hill_climbing_search(search_algorithm.objective_function1)
        if final_state1 == goal_state:
            print("Success using heuristic O1(n)")
            print("Start State:\n", initial_state)
            print("Goal State:\n", goal_state)
            print("Total number of states explored:", states_explored1)
            break
        else:
            print("Failure using heuristic O1(n)")
            print("Start State:\n", initial_state)
            print("Goal State:\n", goal_state)
            print("Total number of states explored before termination:", states_explored1)
        
        # Hill Climbing with Objective Function O2(n)
        final_state2, states_explored2 = search_algorithm.hill_climbing_search(search_algorithm.objective_function2)
        if final_state2 == goal_state:
            print("Success using heuristic O2(n)")
            print("Start State:\n", initial_state)
            print("Goal State:\n", goal_state)
            print("Total number of states explored:", states_explored2)
            break
        else:
            print("Failure using heuristic O2(n)")
            print("Start State:\n", initial_state)
            print("Goal State:\n", goal_state)
            print("Total number of states explored before termination:", states_explored2)

if __name__ == "__main__":
    main()
