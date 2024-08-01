import numpy as np
from copy import deepcopy
from copy import copy
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import random
import matplotlib.pyplot as plt

## Load Data

with open('Sample.tsp') as f:
    file = f.read().split("\n")
    #print(file)
    index=[]
    x=[]
    y = []
    for i in file:
        a , b, c = i.split()
        index.append(int(a)-1) # in here I change city numbers from 1 to m into 0 to m-1 to be same as list index
        x.append(float(b))
        y.append(float(c))
print(index)
print(x)
print(y)

"""## Display Data"""
# plt.style.use('seaborn-whitegrid')
plt.plot(x, y, 'o', color='black');

"""# Implementation

## def HILL-CLIMBING(problem)
- return a state that is a (global) maximum
- input: problem, a problem
- local variables:
    - current, a node.
    - neighbor, a node.

* current = MAKE-NODE(INITIAL-STATE[problem])
* loop do
    * neighbor = a highest valued successor of current
    * if VALUE [neighbor] ≤ VALUE[current] then return STATE[current]
    * current = neighbor

## Compute Distance between 2 cities
"""

def distance(x1,y1 ,x2,y2):
  dis = np.sqrt(np.square(x1-x2) + np.square(y1-y2))
  return dis

print(f"first ({x[0]},{y[0]}) and second ({x[1]},{y[1]})")
distance(x[0],y[0], x[1],y[1])

"""## Make matrix of distance:"""

def tsp_matrix(x,y):
  tsp = []
  row = []
  for i in range(len(x)):
    row.clear()
    for j in range(len(x)):
      row.append(distance(x[i],y[i] ,x[j],y[j]))
    r = copy(row)
    tsp.append(r)
  return tsp

tsp = tsp_matrix(x,y)

for a in tsp:
    print(a)

"""## Make random solution"""

def random_solution(tsp):
  cities = list(range(len(tsp))) #[0,1,..7,,9] len(tsp) = 10
  solution = []

  for i in range(len(tsp)):
    random_city = cities[random.randint(0,len(cities)-1)]
    solution.append(random_city)
    cities.remove(random_city)

  return solution


# test of function

print(random_solution(tsp), '\n', len(random_solution(tsp)))

## Find Route Length"

def route_length(tsp, solution):
  """
  Funciton input is tsp and solution which tsp is matrix of distance between cites and solution is list of cites

  The output is length of solution from firt city to the goal (cost)
  """
  length = 0
  for i in range(len(solution)):
    length += tsp[solution[i-1]][solution[i]]
  return length

# test
tsp = tsp_matrix(x,y)
rands = random_solution(tsp)
print(route_length(tsp,rands))

"""## Find Neighbour"""

def find_neighbors(solution):
  neighbors = []
  for i in range(len(solution)): # 0,1,...9
    for j in range(i+1,len(solution)): # 0 = 1-9, 1= 2-9
      a = solution.copy()
      a[i] = solution[j]
      a[j] = solution[i]
      neighbors.append(a)
  return neighbors


# solution = random_solution(tsp)

"""## Find best neighbour"""

def find_best_neighbor(tsp , neighbors):
  best_neighbor_length = route_length(tsp, neighbors[0]) # Initial answer
  best_neighbor = neighbors[0]

  for i in neighbors:
    current_length = route_length(tsp , i)
    if current_length < best_neighbor_length :
      best_neighbor_length = current_length
      best_neighbor = i

  return best_neighbor, best_neighbor_length

"""## Plot the Cost"""

def plot_cost(cost_value):
  iteration = []
  for i in range(1,len(cost_value)+1):
    iteration.append(i)

  plt.plot(iteration, cost_value, '-o', color='blue');

"""## Hill Climbing"""

def hill_climbing(tsp):

  cost_value = []

  # current  MAKE-NODE(INITIAL-STATE[problem])
  current_solution = random_solution(tsp) # This line of code will give us a random road to all cities
  print(current_solution)
  current_route_length = route_length(tsp,current_solution) # This our cost value for current route
  print(current_route_length)

  print(f"Current solution is {current_solution} with cost of: {current_route_length}")

  # finding neighbors
  neighbors = find_neighbors(current_solution)

  # neighbor  a highest valued successor of current
  best_neighbor , best_neighbor_length = find_best_neighbor(tsp , neighbors)

  # loop do
  # if VALUE [neighbor] ≤ VALUE[current] then return
  while best_neighbor_length <= current_route_length :
    # current = neighbor
    current_solution = best_neighbor
    print(f"Current solution is {current_solution} with cost of: {current_route_length}")
    current_route_length = best_neighbor_length

    cost_value.append(current_route_length)

    # neighbor  a highest valued successor of current
    neighbors = find_neighbors(current_solution)
    best_neighbor , best_neighbor_length = find_best_neighbor(tsp , neighbors)

  return current_solution , current_route_length, cost_value

"""## Main"""

tsp = tsp_matrix(x,y) # This line will give us m*m matrix of distance between cites. m is total number of cities

Best_solution, best_cost , cost_value = hill_climbing(tsp) # This line of code will find best solution with hill_climbing algorithm

print("\n"+ f"Best solution is {Best_solution} and best cost is {best_cost}")

plot_cost(cost_value)
plt.xlabel("iteration")
plt.ylabel("Cost")
# After the plot_cost function call
plt.show()

