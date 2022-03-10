#AdjList:
graph = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2]
]

### With Adjacency List
def traversalBFS(graph): # graph has the shape of our adj list
  seen = {}
  queue = [0]
  res = []

  while queue:
    current = queue.pop(0)
    res.append(current)
    seen[current] = True

    neighbours = graph[current]
    for n in neighbours:
      if n not in seen:
        queue.append(n)
  
  return res

print(traversalBFS(graph))