time_taken_bfs = []
time_taken_dfs = []
step_bfs= []
step_dfs=[]
unreachable_state = []
random_matrix=[]
goal_matrix=[]


import random
def generate_random_matrix():

  random_numlist=[1,2,3,4,5,6,7,8,'X']
  random.shuffle(random_numlist)
  random_matrix = []
  for x in range(0,9,3):
    random_matrix.append(random_numlist[x:x+3])       #converting te random list into 3X3 matix
  goal_matrix = [[1,2,3],[4,5,6],[7,8,'X']]

  return random_matrix, goal_matrix

random_matrix, goal_matrix = generate_random_matrix()



import time

def find_X_position(state):
  xpos = None
  for i in range(3):
    for j in range(3):
      if state[i][j] == 'X':
        xpos = (i,j)

    if xpos:
      break;
  return xpos

def possible_moves(state):
    moves = []
    Xpos = find_X_position(state)

    for dr, dc, move in [(1, 0, 'DOWN'), (-1, 0, 'UP'), (0, 1, 'RIGHT'), (0, -1, 'LEFT')]:
        new_row, new_col = Xpos[0] + dr, Xpos[1] + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[Xpos[0]][Xpos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[Xpos[0]][Xpos[1]]
            moves.append((new_state, move))
    return moves

def sanjeev_apply_bfs(initial_state):
    queue = [(initial_state, [])] # Queue of states with their respective paths
    visited = set() # Set to keep track of visited states

    while queue:
        state, path = queue.pop(0)

        if tuple(map(tuple, state)) in visited:
            continue

        visited.add(tuple(map(tuple, state))) # Convert list of lists to tuple of tuples for hashing

        if state == goal_matrix:
            return path

        for move, direction in possible_moves(state):
            if tuple(map(tuple, move)) not in visited:
                queue.append((move, path + [direction]))

    return False

if __name__ == '__main__' :
  get_start_time = time.time()

  x=0
  while (x <1):
    print("\ninitial state is - ", random_matrix)
    print("target state is - ", goal_matrix)
    result_bfs = sanjeev_apply_bfs(random_matrix)

    if(result_bfs):
      print("number of Steps taken in bfs - ",len(result_bfs))
      step_bfs.append(len(result_bfs))
      x+=1
    else:
      print("unreachable state")
      unreachable_state.append(random_matrix)
      break

  time_taken_bfs.append(round(time.time()-get_start_time, 2))



import random
import time
from collections import deque

# Define the goal state
GOAL_STATE = goal_matrix

# Define possible moves: UP, DOWN, LEFT, RIGHT
MOVES = [(0, -1, 'LEFT'), (0, 1, 'RIGHT'), (-1, 0, 'UP'), (1, 0, 'DOWN')]


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 'X':
                return i, j

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def apply_move(state, move):
    """
    Apply a move to the puzzle state.
    """
    blank_x, blank_y = find_blank(state)
    new_x, new_y, _ = move
    new_state = [row[:] for row in state]  # Make a copy of the state

    # Swap the blank tile with the neighboring tile
    new_state[blank_x][blank_y], new_state[blank_x + new_x][blank_y + new_y] = \
        new_state[blank_x + new_x][blank_y + new_y], new_state[blank_x][blank_y]

    return new_state

def possible_moves(state):
    """
    Find all possible moves from the current state.
    """
    moves = []
    blank_x, blank_y = find_blank(state)

    for dx, dy, move_name in MOVES:
        if is_valid_move(blank_x + dx, blank_y + dy):
            moves.append((dx, dy, move_name))

    return moves

def sanjeev_dfs_search(initial_state):
    """
    Depth-First Search to find a solution to the 8-puzzle problem.
    """
    stack = deque([(initial_state, [])])  # Stack of states with their respective paths
    visited = set()  # Set to keep track of visited states

    while stack:
        state, path = stack.pop()
        if tuple(map(tuple, state)) in visited:
            continue

        visited.add(tuple(map(tuple, state)))  # Convert list of lists to tuple of tuples for hashing

        if state == GOAL_STATE:
            return path

        for move in possible_moves(state):
            new_state = apply_move(state, move)
            if tuple(map(tuple, new_state)) not in visited:
                stack.append((new_state, path + [move[2]]))
    return False

if __name__ == '__main__':
    get_start_time = time.time()

    x = 0
    while x < 1:
        random_state = random_matrix
        print("\nInitial state is - ", random_state)
        result_dfs = sanjeev_dfs_search(random_state)
        if result_dfs:
            print("Number of Steps taken in DFS - ", len(result_dfs))
            step_dfs.append(len(result_dfs))
            x += 1
        else:
            print("Unreachable state")
            unreachable_state.append(random_state)
            break
        try:
          time_taken_dfs(round(time.time() - get_start_time, 2))
        except:
          continue





print(" ------------------------------------------------ \nAverage number of Steps taken in BFS - ",sum(step_bfs) / len(step_bfs))
print(" ------------------------------------------------ \nAverage number of Steps taken in DFS - ",sum(step_dfs) / len(step_dfs))
print("Costs in BFS - ", step_bfs)
print("Costs in DFS - ", step_dfs)
print("Unreachable states in DFS - ", unreachable_state)
print("Total time taken in BFS - ",sum(time_taken_bfs), "seconds")
print("Total time taken in DFS - ",sum(time_taken_dfs), "seconds")