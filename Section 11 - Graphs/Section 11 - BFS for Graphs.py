### With Adjaceny List
def traversalBFS(graph): # graph has the shape of our adj list
  if graph is None:
    return []

  # Create an array in which to store our results
  res = []
  # Create a seen object to save seen nodes
  seen = {}
  # Start the recursion passing down the first node
  recursiveTraverse(0, graph, res, seen)
  return res

def recursiveTraverse(node, graph, res, seen):
  # Append the node passed
  res.append(node)
  # Add it to the seen objecto
  seen[node] = True
  # Get the nodes neighbours
  neighbours = graph[node]
  # Loop over them and start the recursion if not in seen
  for n in neighbours:
    if n not in seen:
      recursiveTraverse(n, graph, res, seen)


### With Adjaceny Matrix
def traversalBFS(graph): # graph has the shape of our adj matrix
  if graph is None:
    return []

  # Create an array in which to store our results
  res = []
  # Create a seen object to save seen nodes
  seen = {}
  # Start the recursion passing down the first node
  recursiveTraverse(0, graph, res, seen)
  return res

def recursiveTraverse(node, graph, res, seen):
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
        recursiveTraverse(n, graph, res, seen)