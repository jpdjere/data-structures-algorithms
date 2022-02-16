# Section 10 - Heaps and Priority Queues

## Introducing Heaps

**Heaps** is a data structure that resembles a **complete binary tree**, where every level is full, except for the last level, which can be full or not. However, if there are nodes in the last level, they must be pushed as much as possible to the left.

![](2022-02-16-11-48-35.png)

There are two variations of **heaps**:

### Max Heaps

![](2022-02-16-11-49-48.png)

A **max heap** has values in it in such way that, at every single node, all of the children of that node have a value smaller than it. As such, the **root** is always the node with **the greatest value**.

Notice that this doesn't guarantee that, for example, the second and third nodes will be the second and third greatest values:

![](2022-02-16-11-52-35.png)

In the example above, we have a node with value of `35` under the node with `40`, while the third node has value `25`, which is less.

### Min Heaps

**Min heaps** are nodes with exactly the reverse rule as **max heaps**: at every single node, all of its children have a value **greater than it**. Therefore, the **root** is always the node with **the minimum value** in the heap.

Now we need to understand how we can add values to our heaps. Let's start with a **max heap** as an example:

![](2022-02-16-14-13-27.png)

First of all, **how do we represent a heap inside of code?**

Up to now, we have been using a tree structure using `node` objects that nestedly point to each other.

For **heaps** we will represent its data using **arrays**, combined with a **BSF approach**:

![](2022-02-16-14-15-15.png)

```py
[50, 40, 25, 20, 35, 10, 15]
```

One **important different** between this array-type of representation of a heap, and the tree with nodes representation that we've seen before is that for array **we need to figure out mathematical formulas tht help to bind the relationship between nodes that we had with our node objects before**.

Before, we could access a node's children directly with their pointers to `left` and `right`, but that doesn't exist with arrays.

So what we want to do now is to think of these relationships relative to the indeces of the elements in our array:

```py
  parent of a node =      floor((index - 1) / 2)
  left child of a node =  index * 2 + 1 
  right child of a node =  index * 2 + 2 
```

Let's look at a couple of examples:

```py
[50, 40, 25, 20, 35, 10, 15]
  0   1   2   3   4   5   6
```

If we want to get the parent node of the node with value `10`:
```
  index of node with value 10 = 5
  parent index = floor((index - 1) / 2 ) = floor((5 - 1) / 2) = floor(2) = 2
  array[2] = 25
```

If we want to get the left child of the node with value `40`:
```
  index of node with value 40 = 1
  left child index = index * 2 + 1 = 1 * 2 + 1 = 3
  array[3] = 20
```

If we want to get the right child of the node with value `25`:
```
  index of node with value 25 = 2
  right child index = index * 2 + 2 = 2 * 2 + 2 = 6
  array[6] = 15
```

## Insertion in Heaps - Understanding Sift Up

Let's learn **how to insert values in a max heap.**

### Conceptual version as a complete binary tree

If we want to insert the value `45` into the heap, what should happen?

![](2022-02-16-18-19-45.png)

Since a **heap** behaves like a **complete binary tree**, we can only insert it at the last available spot following a **BSF** approach:

![](2022-02-16-18-20-44.png)

But once we have inserted our `45` we take a look at the **heap** and ask ourselves: is it still a valid **max heap**?

And in this case, it's not because `45` should be in a higher level.

So the first step is taking `45` and comparing it to its parent. If `45` is greater than the value of its parent (in this case `20`), then **we swap the values** in the nodes:

![](2022-02-16-18-22-50.png)

Once again, we need to compare this node against its parent. So we ask: if `45` greater than `40` (the value of it parent)?

Since it is, we swap their values:

![](2022-02-16-18-24-51.png)

And then we compare again: is the value in our node greater than its parent (in this case, the value in the `root` node)?

No it isn't. So in this case we don't switch the value of the nodes:

![](2022-02-16-18-26-35.png)

And now `45` is in the correct place in the **max heap**:

![](2022-02-16-18-26-59.png)

### Version as an array

The first step to add a new value into a **max heap** in its array representation is to **push it/append it** as the last place in the array:


```py
[50, 40, 25, 20, 35, 10, 15]
  0   1   2   3   4   5   6

[50, 40, 25, 20, 35, 10, 15, 45]
  0   1   2   3   4   5   6,  7
```

But now we need to keep comparing the node's value to the value of it parent to see if it should be switched up.

So first, we take `45` with its index of `7` and try to find its parent:

```py
 parent of index 7 = floor((7 - 1) / 2) = 3
```

Now we can compare the values:

```py
  array[node] >? array[parent] 
  array[7] >? array[3] ===> 45 >? 20  ===> True
```

Since the value at element 7 is greater than the value at element 3, we swap their values:

```py
[50, 40, 25, 45, 35, 10, 15, 20]
  0   1   2   3   4   5   6,  7
```

No we compare again, but now using the index `3`:

```py
  parent of index 3 = floor((3 - 1) / 2) = 1

  array[node] >? array[parent] 
  array[3] >? array[1] ===> 45 >? 40  ===> True
```

Since this condition is true again, we swap our values again:

```py
[50, 45, 25, 40, 35, 10, 15, 20]
  0   1   2   3   4   5   6,  7
```

And we do one more comparison, using index `1`:

```py
  parent of index 1 = floor((1 - 1) / 2) = 0

  array[node] >? array[parent] 
  array[1] >? array[0] ===> 45 >? 50  ===> False
```

And since the codition proves `False`, **we don't need to swap the values, and we stop comparing.**

## Difference in the algorithm between max heap and min heap

The algorithm for **inserting** new values in a **heaps** is exactly the same, except for one main difference.

On insertion, values are added on the last available place and then compared to their parents up the tree (or array). 

The difference is that, while in a **max heap** the values are switched if the inserted value is **greater than the value of its parent**, in a **min heap** the values are switched if the inserted values **is smaller than the value of its parent.**


