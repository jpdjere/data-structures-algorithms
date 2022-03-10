def traversalDFS(graph, shape): # graph has the shape of our adj list
  if graph is None:
    return []

  # Create an array in which to store our results
  res = []
  # Create a seen object to save seen nodes
  seen = {}
  # Start the recursion passing down the first node
  recursiveTraverseMatrix(0, graph, res, seen) if shape == "matrix" else recursiveTraverseAdjList(0, graph, res, seen)
  return res

def recursiveTraverseAdjList(node, graph, res, seen):
  # Append the node passed
  res.append(node)
  # Add it to the seen objecto
  seen[node] = True
  # Get the nodes neighbours
  neighbours = graph[node]
  # Loop over them and start the recursion if not in seen
  for n in neighbours:
    if n not in seen:
      recursiveTraverseAdjList(n, graph, res, seen)

def recursiveTraverseMatrix(node, graph, res, seen):
  # Append the node passed
  res.append(node)
  # Add it to the seen object
  seen[node] = True
  # Get the nodes neighbours
  neighbours = graph[node]
  # Loop over them and start the recursion if not in seen
  for n, val in enumerate(neighbours):
    if val == 1:
      if n not in seen:
        recursiveTraverseMatrix(n, graph, res, seen)

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

def adjListToMatrix(graph):
  newGraph = []
  length = len(graph)
  for idx, val in enumerate(graph):
    newVal = [0] * length
    for i in val:
      newVal[i] = 1
    newGraph.append(newVal)
  return newGraph

print(traversalBFS(graph, "list"))
print(traversalBFS(adjListToMatrix(graph), "matrix"))