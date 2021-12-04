# Section 8 - Data Structures: Linked Lists

## Linked Lists Introduction

We are ging to gro throught two types of linked list: singly and doubly linked lists.

What problems do we encounter with arrays?

With static arrays, we only have a certain amount of memory that can be allocated next to each other. 

Both static and dynamic arrays can increase their data size once they reach a certain limit and double up their size in another location. This operation takes place once every certain amount of time (when the array is about to be full) and has a performance implication: it costs us O(N).

Additionally, arrays have bad performance for operations like insertion or delete which have to shift indeces over, for example at the middle or at the beggining.

Hash table addresses many of this problems but with one big caveat: they don't keep our data in order.

This is where **linked lists** come in to play.

## What is a linked list?

A linked list is a list that is linked.

![](2021-11-30-08-27-07.png)

A linked list is formed by a set of **nodes**. Each **node** has two elements:

- **value**: the data held by the node
- **pointer**: points to the next node in the list.

The first node is called the **head** and the last one is called the **tail**.

Linked lists are **null-terminated**, which means that we know which is the tail node bacause is points to `null`.

Nodes in a list can be sorted, unsorted and they can hold pretty much any data type.

## Why Linked Lists?

Why do you think, from what we know up to know, that linked lists can be better than arrays or hash tables?

Linked Lists have a "loose" structure, that allows you to insert a value into the middle of the linked list, by simply resetting a few pointers. 

In an array, our data is indexed, so retrieving a value from the middle of an array is simple by using the index and has a linear time complexity. However, when trying to find a value somewhere in the linked list, we have to do "traversal" of the whole data structure, starting from the head and following down the pointer to the subsequent nodes until we find our desired value.

Another advantage that arrays might have, is that most computers have cacheing system that makes reading data from sequential memory addresses faster than reading scattered addresses.

So iterating or traversing through a linked list is quite a bit slower than doing so through an array, even though they are techincally both O(N). However, the inserts that we can do in the middle or beggining of the data structure are a lot better than in an array.

The main advantage that linked lists have over hash tables is that we can keep an order for our data values. 

Let's take a look at the time complexity of the main operations for linked lists:

![](2021-11-30-08-45-00.png)

## What is a pointer?

A pointer is a reference to another place in memory.

In Javascript we can see this in action simply:

```js
const object1 = { a: true };

// object2 is a reference to object1
// it does not copy the object, there is only one in memory
const object2 = object1;

object1.a = "New value";
console.log(object1); // { a: "New value" }
console.log(object2); // { a: "New value" }

// If I delete object1
delete object1;
console.log(object1); // undefined
console.log(object2); // { a: "New value" }

// Because object2 is still a pointer to object1,
// even though we deleted object1 itself, the data
// at the memory address of object1 is not garbage
// collected by JavaScript, becuase there is a pointer
// still pointing at it.
```
In other non-garbage collected languages you would have to do this garbage collecting yourself.

## Our First Linked List

Let's create our first linked list with the shape: `10 --> 5 --> 16`.

### Javascript
```js
let myLinkedList = {
  head: {
    value: 10,
    next: {
      value: 5,
      next: {
        value: 16,
        next: null
      }
    }
  }
}

class LinkedLink {
  constructor(value) {
    this.head = {
      value,
      next: null
    }
    this.tail = head;
    this.length = 1;
  }
}

const myLinkedList = new LinkedList(10);
```

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

llist = LinkedList(Node("a"))
print(llist)
```

## Adding append()

### Javascript
```js
class LinkedLink {
  constructor(value) {
    this.head = {
      value,
      next: null
    }
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = {
      value,
      next: null
    }
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }
}

const list = new LinkedLink(5).append(3);
list.append(6);
list.append(99);
console.log(JSON.stringify(list))
```

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

  def append(self, newNode):
    self.tail.next = newNode
    self.tail = newNode
    self.length = self.length + 1
    return self

llist = LinkedList(Node("a")).append(Node("b")) # a -> b -> None
print(llist)
```

## Adding prepend()

### Javascript
```js
class LinkedLink {
  constructor(value) {
    this.head = {
      value,
      next: null
    }
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = {
      value,
      next: null
    }
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    let newNode = {
      value,
      next: this.head
    }
    this.head = newNode;
    this.length++;
    return this;
  }
}

const list = new LinkedLink(5).append(3);
list.append(6);
list.append(99);
list.prepend(-1);
console.log(JSON.stringify(list))
```

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

  def append(self, newNode):
    self.tail.next = newNode
    self.tail = newNode
    self.length = self.length + 1
    return self

  def prepend(self, newNode):
    newNode.next = self.head
    self.head = newNode
    self.length = self.length + 1
    return self

llist = LinkedList(Node("a")).append(Node("b")).prepend(Node("z")) # a -> b -> None
print(llist)
```

## Node Class

In Javascript, we should also have a Node class:
```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class LinkedLink {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    let newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }
}

const list = new LinkedLink(5).append(3);
list.append(6);
list.append(99);
list.prepend(-1);
console.log(JSON.stringify(list))
```

## Adding insert()

### Javascript
```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class LinkedLink {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    let newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while(currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array.join(" --> ");
  }

  insert(index, value) {
    if(index > this.length) {
      return "Error: New index out of bounds."
    }
    if(index === 0) {
      this.prepend(value);
      return this.printList();
    }
    let currentNode = this.head;
    for(let currentIndex = 0; currentIndex < index - 1; currentIndex++) {
      currentNode = currentNode.next;
    }
    const newNode = new Node(value);
    newNode.next = currentNode.next;
    currentNode.next = newNode;
    return this.printList();
  }
}

const list = new LinkedLink(5).append(3);
list.append(6);
list.append(99);
list.prepend(-1);
console.log(list.printList())
list.insert(0, 999)
```

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

  def append(self, newNode):
    self.tail.next = newNode
    self.tail = newNode
    self.length = self.length + 1
    return self

  def prepend(self, newNode):
    newNode.next = self.head
    self.head = newNode
    self.length = self.length + 1
    return self

  # This is a traverse helper function
  # that we will use in insert and remove
  def traverse(self, index):
    counter = 0
    returnNode = self.head
    while counter != index:
      returnNode = returnNode.next
      counter = counter + 1
    return returnNode

  def insert(self, index, newNode):
    # If index passed is larger or equal to length
    # return an out of bounds error
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"
    # Edge case when index is 0, just prepend newNode
    if(index == 0):
      self.prepend(newNode)
    leadNode = self.traverse(index - 1)
    newNode.next = leadNode.next
    leadNode.next = newNode
    self.length += 1
    return self

llist = LinkedList(Node("a")).append(Node("b")).prepend(Node("z")).insert(2, Node("55")) # z -> a -> 55 -> b -> None
print(llist)
```

## Adding remove()

### Javascript
```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class LinkedLink {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    let newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while(currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array.join(" --> ");
  }

  insert(index, value) {
    if(index > this.length) {
      return "Error: New index out of bounds."
    }
    if(index === 0) {
      this.prepend(value);
      return this.printList();
    }
    let currentNode = this.head;
    for(let currentIndex = 0; currentIndex < index - 1; currentIndex++) {
      currentNode = currentNode.next;
    }
    const newNode = new Node(value);
    newNode.next = currentNode.next;
    currentNode.next = newNode;
    return this.printList();
  }

  remove(index) {
    if(index > this.length) {
      return "Error: New index out of bounds."
    }
    if(index === 0) {
      this.head = this.head.next;
      this.length--;
      return this.printList();
    }

    let currentNode = this.head;
    for(let currentIndex = 0; currentIndex < index - 1; currentIndex++) {
      currentNode = currentNode.next;
    }
    let nodeToDelete = currentNode.next;
    currentNode.next = nodeToDelete.next;
    this.length--;
    return this.printList();
  }
}

const list = new LinkedLink(5).append(3);
list.append(6);
list.append(99);
list.prepend(-1);
console.log(list.printList())
list.insert(0, 999)
```

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

  def append(self, newNode):
    self.tail.next = newNode
    self.tail = newNode
    self.length = self.length + 1
    return self

  def prepend(self, newNode):
    newNode.next = self.head
    self.head = newNode
    self.length = self.length + 1
    return self

  def traverse(self, index):
    counter = 0
    returnNode = self.head
    while counter != index:
      returnNode = returnNode.next
      counter = counter + 1
    return returnNode

  def insert(self, index, newNode):
    # If index passed is larger or equal to length
    # return an out of bounds error
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"
    # Edge case when index is 0, just prepend newNode
    if(index == 0):
      self.prepend(newNode)
    leadNode = self.traverse(index - 1)
    newNode.next = leadNode.next
    leadNode.next = newNode
    self.length += 1
    return self

  def remove(self, index):
    # If index passed is larger or equal to length
    # return an out of bounds error
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"
    # Edge case when index is 0, just update the head
    if(index == 0):
      self.head = self.head.next
      self.length -= 1
      return self
    leadNode = self.traverse(index - 1)
    leadNode.next = leadNode.next.next
    self.length -= 1
    return self

llist = LinkedList(Node("a")).append(Node("b")).prepend(Node("z")).insert(2, Node("55")).remove(2).remove(3)
 # z -> a -> 55 -> b -> None
print(llist)
print(llist.length)

```


## Doubly Linked Lists

A doubly linked list is similar to a singly linked list except that each node also links to the node before it.

![](2021-12-03-08-19-08.png)

A doubly linked list allows us to transverse our list backwards, i.e. from the end to the direction of the beginning. In a singly linked list, there is no way for me to know what node comes before a particular node.

So lookup or searching can technically be a little more efficient in a doubly linked list: it can be O(N/2) because we can start from any of the extremes.

The only downside is that we will have to use more memory to store the references to the previous node, for each node.

### Javascript
```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null; // This is new
  }
}
class DoublyLinkedLink {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = new Node(value);
    newNode.prev = this.tail; // This is new
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    let newNode = new Node(value);
    this.head.prev = newNode; // This is new
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while(currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array.join(" <--> "); // Updated
  }

  insert(index, value) {
    if(index > this.length) {
      return "Error: New index out of bounds."
    }
    if(index === 0) {
      this.prepend(value);
      return this.printList();
    }
    let currentNode = this.head;
    for(let currentIndex = 0; currentIndex < index - 1; currentIndex++) {
      currentNode = currentNode.next;
    }
    const newNode = new Node(value);
    const posterior = currentNode.next;
    newNode.next = posterior; // This is updated
    posterior.prev = newNode; // This is new
    newNode.prev = currentNode; // This is new
    currentNode.next = newNode;
    return this.printList();
  }

  remove(index) {
    if(index > this.length) {
      return "Error: New index out of bounds."
    }
    if(index === 0) {
      this.head = this.head.next;
      this.head.prev = null;
      this.length--;
      return this.printList();
    }

    if(index === this.length - 1) {
      this.tail = this.tail.prev;
      this.tail.next = null;
      this.length--;
      console.log(list)
      return this.printList();
    }

    let currentNode = this.head;
    for(let currentIndex = 0; currentIndex < index - 1; currentIndex++) {
      currentNode = currentNode.next;
    }
    const nodeToDelete = currentNode.next;
    const newNext = nodeToDelete.next;
    currentNode.next = newNext;
    newNext.prev = currentNode;
    this.length--;
    return this.printList();
  }
}
```

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None # This is new

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " <-> ".join(nodes)

  def append(self, newNode):
    self.tail.next = newNode
    newNode.prev = self.tail # This is new
    self.tail = newNode
    self.length = self.length + 1
    return self

  def prepend(self, newNode):
    newNode.next = self.head
    self.head.prev = newNode # This is new
    self.head = newNode
    self.length = self.length + 1
    return self

  def traverse(self, index):
    counter = 0
    returnNode = self.head
    while counter != index:
      returnNode = returnNode.next
      counter = counter + 1
    return returnNode

  def insert(self, index, newNode):
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"

    if(index == 0):
      self.prepend(newNode)

    leadNode = self.traverse(index - 1)
    posteriorNode = leadNode.next  # This is new
    newNode.next = posteriorNode
    posteriorNode.prev = newNode  # This is new
    newNode.prev = leadNode  # This is new
    leadNode.next = newNode
    self.length += 1
    return self

  def remove(self, index):
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"

    if(index == 0):
      self.head = self.head.next
      self.length -= 1
      return self
    leadNode = self.traverse(index - 1)
    posteriorNode = leadNode.next.next  # This is new
    leadNode.next = posteriorNode
    posteriorNode.prev = leadNode  # This is new
    self.length -= 1
    return self

llist = LinkedList(Node("a")).append(Node("b")).prepend(Node("z")).insert(2, Node("55")).remove(2)
 # z -> a -> 55 -> b -> None
print(llist)
print(llist.length)
```

## Singly vs Doubly Linked List

When to use each?

The pros of a singly linked list:
- it is a fairly simple implementation (especially compared to doubly linked)
- requires less memory
- a bit faster because less operations per data structure operation

Cons of a singly linked list:
- Cannot be iterated in reverse.

So use when:
- memory is a limiting factor
- main goal is fast insertion and deletion (and no a lot of searching)

The pros of a doubly linked list:
- It can be iterated from the front or from the back.
- If you need to delete a previous node, you don't need to iterate from the head node all the way to it, you already have the reference from the current node.

Cons of doubly linked list:
- More complex to implement.
- Requires more memory than a singly linked list.
- Requires more operation per DS operation (so also a little slower).

## Implementing reverse()

Reversing a **singly linked list**:

# Javascript
```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class LinkedLink {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    let newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    let newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while(currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array.join(" --> ");
  }

  reverse() {
    if(this.length <= 1) {
      return this.printList();
    }
    // Take first and second nodes
    const first = this.head;
    const second = first.next;

    // Update the tail to be our current head
    this.tail = first;

    // Loop until we reach the end
    while(second) {
      // Take auxiliary the following to second
      const followSecond = second.next;
      // Update the next to second to be our first
      second.next = first;

      first = second
      second = followSecond
    }
    // After finishing looping, remove the reference
    // of our original head to a next
    this.head.next = null;
    // Set an updated head
    this.head = first;
    return this.printList();
  }
```

# Python

### Python
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node
    self.tail = node
    self.length = 1
  
  def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

  def append(self, newNode):
    self.tail.next = newNode
    self.tail = newNode
    self.length = self.length + 1
    return self

  def prepend(self, newNode):
    newNode.next = self.head
    self.head = newNode
    self.length = self.length + 1
    return self

  def traverse(self, index):
    counter = 0
    returnNode = self.head
    while counter != index:
      returnNode = returnNode.next
      counter = counter + 1
    return returnNode

  def insert(self, index, newNode):
    # If index passed is larger or equal to length
    # return an out of bounds error
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"
    # Edge case when index is 0, just prepend newNode
    if(index == 0):
      self.prepend(newNode)
    leadNode = self.traverse(index - 1)
    newNode.next = leadNode.next
    leadNode.next = newNode
    self.length += 1
    return self

  def remove(self, index):
    # If index passed is larger or equal to length
    # return an out of bounds error
    if(index >= self.length):
      return "Index "+str(index)+" out of bounds"
    # Edge case when index is 0, just update the head
    if(index == 0):
      self.head = self.head.next
      self.length -= 1
      return self
    leadNode = self.traverse(index - 1)
    leadNode.next = leadNode.next.next
    self.length -= 1
    return self

llist = LinkedList(Node("a")).append(Node("b")).prepend(Node("z")).insert(2, Node("55"))
 # z -> a -> 55 -> b -> None
print(llist)
print(llist.length)

llist.reverse()
print(llist) # b -> 55 -> a -> z -> None

```