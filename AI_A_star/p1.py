import heapq
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

    def __lt__(self, other):
        # This method is used to define the comparison between PuzzleState objects
        # We'll compare their grids lexicographically
        return self.grid < other.grid

    def __hash__(self):
        return hash(str(self.grid))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])

# --------------------------------------------------------------------------------------------------------------------------

class AStarSearch:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.closed_list = set()

    def h1(self, state):
        # Heuristic h1: Always return 0
        return 0

    def h2(self, state):
        # Heuristic h2: Number of tiles displaced from their destined position
        displaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if state.grid[i][j] != self.goal_state.grid[i][j]:
                    displaced_tiles += 1
        return displaced_tiles

    
    def h3(self, state):
    # Heuristic h3: Sum of the Manhattan distance of each tile from the goal position
        distance = 0
        for i in range(3):
            for j in range(3):
                if state.grid[i][j] != 'B':
                    tile = int(state.grid[i][j])
                    goal_position = self.find_goal_position(tile)
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
            else:
                # Adding the cost of the empty tile as another tile
                distance += abs(i - 2) + abs(j - 2)
        return distance

    

    def h4(self, state):
        # Heuristic h4: Devise a heuristic such that h(n) > h*(n)
        # In this example, let's simply return a constant value greater than the maximum possible h3(n)
        return 25
    
# --------------------------------------------------------------------------------------------------------------------------
    def find_goal_position(self, tile):
        for i in range(3):
            for j in range(3):
                if self.goal_state.grid[i][j] == str(tile):
                    return (i, j)

    def g(self, state):
        # Least cost from the source to the current state
        # Here, it's the number of moves made to reach the current state
        return 0  # Assuming initial state, so g(n) is 0

    def f(self, state, heuristic):
        # f(n) = g(n) + h(n)
        return self.g(state) + heuristic(state)

# ---------------------------------------------------------------------------------------------------------------------------

    def a_star_search(self, heuristic):
        open_list = [(self.f(self.initial_state, heuristic), self.initial_state)]
        closed_list = set()
        states_explored = 0

        while open_list:
            _, current_state = heapq.heappop(open_list)
            states_explored += 1

            if current_state == self.goal_state:
                return True, states_explored  # Goal state reached

            closed_list.add(current_state)

            # Generate successors
            successors = self.generate_successors(current_state)

            for successor in successors:
                if successor not in closed_list:
                    heapq.heappush(open_list, (self.f(successor, heuristic), successor))

                    # Step 4: Verify monotone restriction
                    if not self.monotone_restriction(current_state, successor, heuristic):
                        print("Monotone restriction violated.")

        return False, states_explored  # Goal state not reachable
    
    def verify_monotonicity(self, heuristic):
        # Check if the monotone restriction holds for the closed list of states
        for state, successor in zip(list(self.closed_list)[:-1], list(self.closed_list)[1:]):
            if not self.monotone_restriction(state, successor, heuristic):
                print("Monotone restriction violated.")
                break
        else:
            print("Monotone restriction satisfied.")
    
    def monotone_restriction(self, current_state, successor, heuristic):
        # Check if monotone restriction is satisfied: h(n) <= cost(n,m) + h(m)
        return heuristic(current_state) <= self.g(successor) - self.g(current_state) + heuristic(successor)

# -------------------------------------------------------------------------------------------------------------------------

    def generate_successors(self, state):
        successors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        blank_i, blank_j = state.blank_position
        for di, dj in directions:
            new_i, new_j = blank_i + di, blank_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_grid = [row[:] for row in state.grid]
                new_grid[blank_i][blank_j], new_grid[new_i][new_j] = new_grid[new_i][new_j], new_grid[blank_i][blank_j]
                successors.append(PuzzleState(new_grid))

        return successors

# -----------------------------------------------------------------------------------------------------------------------
def create_random_state():
    numbers = list(map(str, range(1, 9)))  # Convert integers to strings
    numbers.append('B')
    random.shuffle(numbers)
    return PuzzleState([numbers[:3], numbers[3:6], numbers[6:]])

initial_state = create_random_state()

goal_state = PuzzleState([
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', 'B']
])

# -------------------------------------------------------------------------------------------------------------------------

search_algorithm = AStarSearch(initial_state, goal_state)

# Perform A* search using different heuristics
heuristics = [
    (search_algorithm.h1, "h1"),
    (search_algorithm.h2, "h2"),
    (search_algorithm.h3, "h3"),
    (search_algorithm.h4, "h4")
]

# ---------------------------------------------------------------------------------------------------------------------------------------

for heuristic, heuristic_name in heuristics:
    success, states_explored = search_algorithm.a_star_search(heuristic)
    if success:
        print(f"Success using heuristic {heuristic_name}")
        print("Start State:\n", initial_state)
        print("Goal State:\n", goal_state)
        print("Total number of states explored:", states_explored)
    else:
        print(f"Failure using heuristic {heuristic_name}")
        print("Start State:\n", initial_state)
        print("Goal State:\n", goal_state)
        print("Total number of states explored before termination:", states_explored)

    # Verify monotone restriction
    search_algorithm.verify_monotonicity(heuristic)
