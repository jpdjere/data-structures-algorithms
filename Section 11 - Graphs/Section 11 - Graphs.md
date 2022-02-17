# Section 11 - Graphs

## Graphs Introduction

**Graphs** are one of the most used data structures used in Computer Science to modle real life data.

A **graph** is a set of values, which are related in a pair-wise fashion.

In a graph, each item is called **a node (or vertex)**:

![](2022-02-17-09-51-17.png)

Nodes are connected among themselves trhough **edges**:

![](2022-02-17-09-52-33.png)

Graphs are great for modelling real life relationships, representing links, for example data connected among itself.

For example, graphs can be used to represent friendship networks, networks in the World Wide Web, or roads in a map.

Of course, **trees** and even **linked lists** are special types of graphs.

## Types of Graphs

### Directed vs Undirected

![](2022-02-17-09-55-29.png)

**Directed:** edges in a directed graph have a predefined direction (which can be one way, the other way, or the two ways).

**Undirected:** edges have no predefined direction and movement can happen in both ways.

### Weighted vs Unweighted

![](2022-02-17-09-58-24.png) 

**Weighted:** values can be applied to the edges of the graph, giving each "movement" across the edge a weight, cost, penalty, priority, etc.

**Unweighted:** values cannot be applied to the edges of the graph. 

### Cyclic vs Acyclic 

![](2022-02-17-10-13-22.png)

**Cyclic:** the graph has vertices connected in a circular fashion. That's a **cycle**. They are really common in **weighted** graphs, like the ones used in Google Maps.

**Let's now classify a couple of graphs:**

![](2022-02-17-10-13-55.png)

Undirected Cyclic Unweighted

![](2022-02-17-10-14-33.png)

Undirected Cyclic Weighted

![](2022-02-17-10-14-55.png)

Directed Acyclic Unweighted

![](2022-02-17-10-15-21.png)

Direced Acyclic Weighted

![](2022-02-17-10-15-55.png)

**Directed Acyclic Graph** (DAG) -- Also unweighted.

## Graph Data

We aleady know the tools to build graphs: we have built already **trees** and **linked lists**.

Let's attempt to build the following graph:

![](2022-02-17-10-22-15.png)

There are different ways in which you can build graphs:

### Edge List

Draws out the connections between nodes in a list:

```py

graph = [[0, 2], [2, 1], [2, 3], [1, 3]]

```

### Adjacency List

We create an array (or object) where the index is the node's value (in this case), and then we detail its connections:

```py
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

graph = {
  0: [2],
  1: [2, 3],
  2: [0, 1, 3],
  3: [1, 2]
}
```

### Adjacency Matrix

Uses a matrix to show which node is connected to which other node:

```py
graph = [
  [0, 0, 1, 0],
  [0, 0, 1, 1],
  [1, 1, 0, 1],
  [0, 1, 1, 0]
]

graph = {
  0: [0, 0, 1, 0],
  1: [0, 0, 1, 1],
  2: [1, 1, 0, 1],
  3: [0, 1, 1, 0]
}
```

All of these 3 types of representation can be seen in **VisuAlgo**:

![](2022-02-17-10-35-54.png)

## Graph Implementation

```py
class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacencyList = {}

  def addVertex(self, node):
    pass

  def addEdge(self, node1, node2):
    pass

  # Provided helper function
  def showConnections(self):
    adjList = self.adjacencyList
    for key in adjList:
      nodeConnections = adjList[key]
      connections = ""
      for vertex of nodeConnections:
        connections += vertex + " "
      print(node + " --> " + connections)

graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addEdge('3', '1')
graph.addEdge('3', '4')
graph.addEdge('4', '2')
graph.addEdge('4', '5')
graph.addEdge('1', '2')
graph.addEdge('1', '0')
graph.addEdge('0', '2')
graph.addEdge('6', '5')
graph.showConnections()
```

Complete the `addVertex` and `addEdge` implementations:

```py
class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacencyList = {}

  def addVertex(self, node):
    self.numberOfNodes += 1
    self.adjacencyList[node] = []

  def addEdge(self, node1, node2):
    pass

  # Provided helper function
  def showConnections(self):
    adjList = self.adjacencyList
    for key in adjList:
      nodeConnections = adjList[key]
      connections = ""
      for vertex of nodeConnections:
        connections += vertex + " "
      print(node + " --> " + connections)

graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addEdge('3', '1')
graph.addEdge('3', '4')
graph.addEdge('4', '2')
graph.addEdge('4', '5')
graph.addEdge('1', '2')
graph.addEdge('1', '0')
graph.addEdge('0', '2')
graph.addEdge('6', '5')
graph.showConnections()
```