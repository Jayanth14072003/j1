from sys import maxsize
from itertools import permutations
V = 4
def tsp(graph, s):
 vertex = []
 for i in range(V):
  if i!=s:
   vertex.append(i)
 min_cost = maxsize
 next_permutation = permutations(vertex)
 for i in next_permutation:
  current_cost = 0
  k = s
  for j in i:
   current_cost += graph[k][j]
   k = j
 current_cost += graph[k][s]
 min_cost = min(min_cost, current_cost)
 return min_cost
graph = [
 [0,10,20,15],
 [10,0,30,35],
 [20,30,0,25],
 [15,35,25,0]
]
s = 0
print(tsp(graph, s))
