# Maximum Depth of Binary Tree (Easy)

Given a binary tree, find its maximum depth.

Maximum depth is the number of nodes along the longest path from the root node to the furthest leaf node.

![](2022-01-31-21-59-27.png)

## Step 1: Verify the Constraints

1. What do we return if the tree is empty?

Return 0

## Step 2: Write out some test cases

![](2022-01-31-22-01-26.png)
The above tree should return **5**

![](2022-01-31-22-02-01.png)
The above tree should return **0**

![](2022-01-31-22-02-23.png)
The above tree should return **1**

But, we should also consider a worst-case:
![](2022-01-31-22-03-02.png)
The above tree should return **5**, but this test case is important to make us realized that the time and space complexity of this solution will be **O(N)**. We'll take a look at why later.

## Learning the Process for Solving Binary Tree Problems

Let's take a look at the questions that one should ask when solving BT problems. Most BT questions have a lot overlap in the way you should approach them, so these questions are usually valid for a great majority of them.

1. **Should I traverse this tree?**

This question usually has a **YES** answer for most problems, but there are certain cases in which traversal is actually not needed.

In this specific problem, we DO need to traverse the tree, because we need to find the maximum depth of the tree and there's no other way to do that.

2. **How should I traverse this tree? (BFS or DFS)**

Knowing that I should traverse this tree, I can choose between BFS and DFS. Knowing that with BFS we attempt to find nodes that are closer rather than further to the root, and understanding that in this problem we need to find the node than is further away from the root, we can discard BFS as a technique and concentrate on DFS, which assumes the node that we are searching for is probably at the end of the path that it is searching.

It is still possible, in this exercise, that the node that we are looking for is found at the last path that DFS explores, but it is very likely that we will get one of this last nodes first thorught DFS rather than finding them through BFS.

Now that that we have chosen DFS, we should normally think about which Traversal Type to use (Preorder, Inorder, Post-order). However, since the traversal type relates to how we examine, store or use the values insides the nodes, and that in this case we don't care about the values of the nodes, we don't need to make a decision.

3. **Let's break down DFS**

DFS is recursive by nature. And when it comes to coming up with a recursive solution for a binary tree question, we want to think about the logical step you want to do in the recursion before writing code. It is easier to let the nature and anatomy of the recursion of the recursive function guide your logical solution, than trying to solve a logical solution without recursion. (Iterative solutions for BST questions are much more complicated. And recursive solutions are enough to pass.)

So: remember that a recursive function calls itself over and over until it hits a base case, which returns a value, and then, using all those accumulated values, comes up with a final answer.

The recursive call that we need for this DFS traversal **will always pass one of the current children** to itself, on the left or the right. So we know that the first argument that we are getting in the recursive function is a node.

The first node we are getting, in the first recursive call, will always be the root node (or null if there is no tree). The next one would be its left or right child.

Are there any additional arguments passed down to the recursive function? It is highly possible that there might be, so let's think about it taking a look at the pseudo code we have up to now:

```py
def recursive(node,   ):
  ...
```

What else is involved in a recursive call? We know we have **base cases**. It might be one or more, but its main goal is to say "i'm done calling the recursive function", I have an answer. This answer might not be the final or complete answer, but a part of an full and complete answer that you are working towards to.

```py
def recursive(node,   ):
  base case
```

The goal or answer in this case is to count the number of nodes that we have traversed, vertically. We are DF Searching, counting the nodes along the way, so we need to keep a **count** of the number of nodes that we've seen along the way. It will initially start at 0, but already in the first recursive call, corresponding to the root, it would need to step up to 1.

Now let's think about recursive calls. Since DFS involves passing down the current node's children to the recursive function, we know that we will pass either the left or the right nodes, (or both! we don't know yet) child, to the recursion:

```py
def recursive(node,   ):
  base case

  recursive(node.left)
  recursive(node.right)
```

To figure out whether we need to pass either the left, the right or both, let's think again: what's the goal that we want to achieve? We want to figure out how the maximum path down one of its children is going to be. But since at this point we don't know how the structure of the tree looks like, we need to extensively search all pathes to both the left and right of the current node, in order to be certain that we have explored all possible paths. So we now know we need to **both** recurse to the left **and** to the right.

```py
def recursive(node,   ):
  base case

  recursive(node.left) AND recursive(node.right)
```

But what are we doing, as we are recursing? We are trying to keep track of the number of nodes that we have been through by the time we have reached the current node. What that means is that **we want to pass down the count from the previous iteration**, both to the left and to the right:

```py
def recursive(node, count):
  base case

  recursive(node.left, count) AND recursive(node.right, count)
```

Now that we have figured out our recursive call, let's think about our base case: if we are doing DFS, we know that we are done searching when we reached a point in which there are no more node to traverse downwards down the tree. That means that whenever **the current node (that has been passed to the recursive function) is null, we have finished our recursive calling, i.e. found one of our base cases**.

If that's the case, what we want to say, is that: when the node that we get as parameter is equal to NULL, then what are we doing? We already know that the `count` that we get as parameter is **maximum number of nodes that we have seen UNTIL we reached this point**.

So for example, if we are currently on the node that is marked with an arrow in the following diagram, we know that the amount of nodes that we have previously seen is 3:

![](2022-02-06-10-49-30.png)

But sine the current place we are at is a node (and not null), then the current count should increase:

![](2022-02-06-10-50-24.png)

But now let's say we traverse to its left. We want to recursively go down the left path: and now we see that when we reach this point (passing down the non-existing node -or null- and passing down also the count which is 4), we shouldn't increase the count anymore, since there is no node. That means that **we just want to return the count that we have got this far, before increasing the count.** So 4 will be returned to its parent node:

![](2022-02-06-10-53-32.png)

Now, tha path on the right, does it has more to count? Yes. So when we recursively call the right child, we see that there is a node, so the count increases to 5. 

![](2022-02-06-10-55-58.png)

From this point, passing down the count to its children, we'll see that there's both a null on the left and right paths, so the 5 will get returned to its parent.

![](2022-02-06-10-57-11.png)

From here, what do we know? We know that both our recursion on the left and on the right have finished, and that we have now available the two values that have been returned, which represent the largest length of path that has been traversed, both on the right and on the left.

Since we want to return only the maximum length of the path, we should **return the maximum value that was returned by those two recursive calls**. And this is another base case:

![](2022-02-06-11-01-09.png)

As you can see also from the diagram above, that value of 5 gets returned to its parent node, and in that level the values of 4 and 5 (returned by the left and right paths, respectively) get compared to get the max value out of the two, and then the max value gets subsequently returned up the tree.

![](2022-02-06-11-02-44.png)

This logic is continued up the tree, until we are back at the root level and we compare the length of the tree that was calculated down its left and right paths.

Let's finish the code:

```py
def recursive(node, count):
  if node is None:
    return count

  count += 1
  return max(recursive(node.left, count), recursive(node.right, count))
```

## 4. Space and Time Complexity

In a worst case scenario, we can imagine that the tree that we have on the diagrams above is flipped, so that the longest path was on the right side, the last node (the deepest one in the tree), would be the last node that our DFS traversal would explore.

That would mean that we essentially **end up exploring every single node inside of the tree**. So in that case, our **time complexity is O(N)**, N being the total number of nodes in the tree,

What about Space Complexity?

**Space Complexity is going to be the size of our recursion:** in the example with this binary tree, our recursive call can get as large as five, because we have five levels of tree. So we can see this as a case where **the height of the tree is the size of the recursion**.

In a perfectly balanced tree, the **height of the tree is log N**, so the space complexity would be **O(log N)**.

But what about the worst case? If we have a fully unbalanced tree, like:

![](2022-02-06-11-13-49.png)

Then in this case, the **height of the tree is N**. So if we are recursively calling every single child of every single node, our recursive stack is the size of the tree, which will end up being N. 

So in **the worst-case scenario, space complexity will be O(N)**.

**Time Complexity: O(N)**
**Space Complexity: O(N)**

### Leetcode Solution:

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root, 0)
        
    def recursive(self, node, count):
        if node is None:
            return count
        
        count += 1
        return max(self.recursive(node.left, count), self.recursive(node.right, count))
```        
.

.

.

.

.

---
# Invert a Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

![](2022-02-06-11-50-38.png)

Constraints:

```
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

## My solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursive(root)
        return root
    
    def recursive(self, node):
        if node is None:
            return node
        
        self.recursive(node.left)
        self.recursive(node.right)
        
        left = node.left
        right = node.right
        node.left = right
        node.right = left
```
.

.

.

.

.

---

# Level Order Traversal of Binary Tree (Medium)

https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the *level order* traversal of the nodes' values, as an array. 

## Explanation

What is *level-order?* 

The question wants us to return an array, in which **each element is an array containing the values of the nodes of its respective level**:

![](2022-02-06-11-55-16.png)

## Step 1: Verify our constraints

What do we return if the tree is empty?

Return an empty array.

## Step 2: Write out some test cases

1. The tree with diagram:

![](2022-02-06-11-59-05.png)

Should return: 
```
[[3], [6, 1], [9, 2, 4], [5], [8]]
```


2. The tree with diagram:

![](2022-02-06-12-00-29.png)

Should return: 
```
[[3]]
```

3. The tree with diagram:

Should return:
```
[]
```

4. We should also consider, for space and time complexity reasons, a tree with the shape of:

![](2022-02-06-12-04-20.png)


## Walking through our solution

Let's tackle this question with the same approach as last problem.

1. Do we need to traverse this tree?

Yes, we need to accumulate the values in arrays within an array.

2. Do we want to use BFS or DFS?

Because of the order in which our data is asked, we should use BFS.

Now that we knoew that **BFS** is the apporach that we want to use, we have to think if it's enough to get to our solution or we have to modify it in some way: BFS would get us the data that we want in an array, but they wouldn't be split by level as the question requires us to do.

Because of this, we have to keep in mind the technical implementation of BFS (or of DFS, in the cases in which that is the approach to use), so that we can succesfully modify them to achieve the answers that we want.

Let's first of all remember the technical implementation of **BFS** in its recursive form, before getting into the details of how to modify it:

```py
def breadthFirstSeachIterative(root):
  res = []
  q = [root]
  while len(q) > 0:
    currentNode = q.pop(0)
    res.append(currentNode.val)
    if currentNode.left is not None:
      q.append(node.left)
    if currentNode.right is not None:
      q.append(node.right)
  return res
```

The above standard implementations of BSF would return us the following array:
```py
[3, 6, 1, 9, 2, 4, 5, 8]
```

As you can see, normal BSF does not care what level the node it is when it adds it to the array. Now we can think how to modify this traditional **BSF** in order to achieve our desired result that should be:
```py
[[3], [6, 1], [9, 2, 4], [5], [8]]
```

So we need to figure out a way to add that to our existing solution.

Instead of just appending the values to `res` we need to create an intermediate array on a per level basis, push the values to that array, and then append that array to res.

So there are three steps that need to be added to the normal BSF solution:

1. **Identify level of tree**
2. **Initialize our currentLevel array**
3. **Push currentLevel array into our global result**

So first, let's identify the level of tree. In order for us to know wether we are at some new level of the tree, we need to figure out whether we are done with the previous level of the tree.

Taking a look at the `while` loop in our code, we know that its going to clear through the queue (q). But let's think what happens when we run BSF in the first place:

We start with q containing only our root node:

```py
q = [root]
```

Here we know that we are on the top level, which only contains the root. When we pop this root value, our while loop is just running through the first iteration; we check if there is a left or right child and we append it to the queue:

```py
q = [6 , 1]
res = [root]
```

At this point, our loop over the queue will just keep running, it doesn't know that we are on a new level. But we know that when, for example, we are done with the root level, we start a new level (which contains 6 and 1). How do we tell our queue that we are on a new level?

What we can say is that, perhaps, when our queue has processed the number of elements that it had when it started the loop, when it was the root value alone in q: 

```py
q = [root]
```

At this moment, what's the size of the queue? In this moment, the size of the queue is 1. So the moment that 1 value has been processed, we know that the first level has been completed. Every following value from the queue is technically the next level.

Let's try that logic:

```py
q = [root]

q.size = 1
```

After processing the root, the only one element in the size of the queue, we are done with the first level. When we process each level, we now know that the values that are processed in each level should be popped into a `currentLevel` array.

```py
q = []

q.size = 1   ---> Level 1

processedCounter = 1

currentLevel = [root]
```

So now we step forward, we check on the root's children, add them to the queue, so that no we have 6 and 1 in our queue, and the size is 2. So we keep a counter that keeps track of how many values from the queue we have processed:

```py
q = [6, 1]

q.size = 2 ---> Level 2

processedCounter = 0

currentLevel = []
```

Next, the 6 is popped into the while-loop, we increment the count by 1 and we add the 6's children to the queue:

```py
q = [1, 9, 2]

q.size = 2 ---> Level 2

processedCounter = 1

currentLevel = [6]
```

Now that we are done with the 6, we repeat for the next value in the queue, the 1, which still belong to level 2, adding its children to the queue (null is ignored, 4 is added):

```py
q = [9, 2, 4]

q.size = 2 ---> Level 2

processedCounter = 2

currentLevel = [6, 1]
```

At this point, our `processedCounter` is equal to the size of our `queue`, so that means that the `currentLevel` is full, and all following values in the `queue` correspond to the next level, and when those values are processed, they should be included into a brand new `currentLevel` array.

Let's continue:

```py
q = [9, 2, 4]

q.size = 3 ---> Level 3

processedCounter = 0

currentLevel = []
```

We first pop up the 9 into our `currentLevel` array, process it, increment our count by one, push its only child into the queue:

```py
q = [2, 4, 5]

q.size = 3 ---> Level 3

processedCounter = 1

currentLevel = [9]
```

We do the same now for the following two elements in the queue (2 elements before our `processedCounter` reaches `q.size`) - notice that none of the following have children, so nothing is added to the queue:

```py
q = [4, 5]

q.size = 3 ---> Level 3

processedCounter = 2

currentLevel = [9, 2]
```

And next:

```py
q = [5]

q.size = 3 ---> Level 3

processedCounter = 3

currentLevel = [9, 2, 4]
```

Now that `processedCounter` is equal to `q.size` we know we are at the end of the level, and our `currentLevel` array should be added to our final `res` array.

On the next step, we see that the size of our queue is equal to 1, which is exactly the amount of elements that we have on the next level:

```py
q = [5]

q.size = 1 ---> Level 4

processedCounter = 0

currentLevel = []
```

And after 1 loop of processing we are done with level 4:

```py
q = [8]

q.size = 1 ---> Level 4

processedCounter = 1

currentLevel = [5]
```

Notice that our `currentLevel` array should be initialized when we are at the start of a level, and that `currentLevel` should be added to our global result when we are at the end of that level. 

And we know that **we are at the start of a level when `processedCounter` is 0; and that we are at the end of a level when `processedCounter` is 1.**



