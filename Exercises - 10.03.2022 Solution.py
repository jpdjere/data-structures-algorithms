#> Strings: Reverse a string

'''
Create a function that reverses a string it gets as an input.
'''

def reverse(text):

#> Arrays: Merge Sorted Arrays

def mergeSortedArrays(arr1, arr2):

#> Arrays: Two Sum

'''
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
``` 

Constraints:
```
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
```
'''

def twoSum(arr, target):


  
#> Excercise: Longest Palindromic Substring

'''
Given a string `s`, find the longest palindromic substring in `s`.

You **may** assume that the maximum length of `s` is 1000.

Example 1:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

Example 2:

```
Input: "cbbd"
Output: "bb"
```

Constraints:
```
1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

def findLongestPalindromicSubstring(s):

https://leetcode.com/problems/longest-palindromic-substring/discuss/751188/Simple-Easy-to-Follow-Python


#> Arrays: Maximum Subarray

'''
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Example 2:
```
Input: nums = [1]
Output: 1
```

Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

Constraints:
```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
```
˚˝˝˚

'''

def maxSubArray(nums):




#> Arrays: Move Zeroes
'''
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Example 2:
```
Input: nums = [0]
Output: [0]
 ```

Constraints:
```
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
```
'''

def moveZeroes(self, nums: List[int]) -> None:




#> Arrays: Rotate Array (Medium)
'''
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

Explanation: 

rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:
```
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
```
'''

def rotate(nums: List[int], k: int) -> None:


#> Arrays: Container with Most Water
'''
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains 
the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container. 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''

def containerWithGreatestArea(arr):






#> Arrays: Trapping Rainwater
'''
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Example 3, 4, 5 and 6:
[0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2] -> 8

[] -> 0

[3] -> 0

[3, 4, 3] -> 0
'''
def trappingRainwater(heights):



#> Arrays: Best Time to Buy and Sell Stock (Easy)
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 

If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        # Keep track of two variables: minPrice and maxProfit
        # Since we only care about lowest peak and hightest valley
        minPrice = math.inf
        maxProfit = 0
        for price in prices:
            # First check if we have a new max profit, comparing our
            # old maxProfit againt the (currentPrice - minPrice -from previous iterations-)
            maxProfit = max(maxProfit, price - minPrice)
            # Only after calculating the maxProfit, update the minPrice, for future iterations
            if price < minPrice:
                minPrice = price
        return maxProfit

# Time Complexity O(N)  ---> One pass
# Space Complexity O(1)  ----> Only two variables           



#> Arrays: Best Time to Buy and Sell Stock II (Medium)
'''   
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        # Keep track of two variables: minPrice and maxProfit
        # Since we only care about lowest peak and hightest valley
        # (nevertheless, minPrice can be resetted to find local minimums)
        minPrice = math.inf
        maxProfit = 0
        for price in prices:
            # First check if we have a new max profit, comparing our
            # old maxProfit against the sum of our current maxProfit + our new profit
            # newLocalProfit = price - minPrice
            if maxProfit + price - minPrice > maxProfit:
              maxProfit = maxProfit + price - minPrice
              # If we have udpated our maxProfit, we have found a new peak, so we should
              # reset our minPrice, so that we can find a new local minimum price for future checks
              minPrice = math.inf
            # Only after calculating the maxProfit, update the minPrice, for future iterations
            if price < minPrice:
                minPrice = price
        return maxProfit
        



#> Arrays: Best Time to Buy and Sell Stock III (Hard)
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
 
Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 105
'''
class Solution:
  def maxProfit(self, prices: List[int]) -> int:




#> Arrays: 3Sum (Medium)
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
    #         return []
    #     target = 0
    #     triplets = []
    #     for idx, num in enumerate(nums):
    #         remaining = target - num
    #         possibleComplementArray = self.twoSum(nums[0:idx] + nums[idx + 1], remaining)
    #         possibleComplement = sum(possibleComplementArray)
    #         if remaining + possibleComplement == 0:
    #             triplets.append([num]+possibleComplementArray)
    #     return triplets

    # # [-1, 3, 4] target = 3
    # def twosum(self, nums, target):
    #     seen = {}
    #     for num in nums:
    #         complement = target - num
    #         if complement in seen:
    #             return [num, complement]
    #         else:
    #             seen[complement] = True # seen[3 - -1] = seen[4] = True
    #     return []
            



            




#> Hashtables: First Recurring Character

'''
Given an array:

array = [2, 5, 1, 2, 3, 5, 1, 2, 4];

Find the first recurring character. The above array should return 2.

'''
def findFirstRecurring(nums):





#> Linked Lists: Implement a Singly Linked List

class Node:

class LinkedList:
  def __init__(self):
  def append(self):
  def prepend(self):
  def traverse(self):
  def insert(self):
  def remove(self):

#> Linked Lists: Reverse a Singly Linked List (Easy)

class Node:

class LinkedList:
  def reverse(self):

#> Linked Lists: M, N reversals (Reverse Linked List II) (Medium)
"""
https://leetcode.com/problems/reverse-linked-list-ii/

Given numbers M, N, reverse only nodes M through N of a linked list.
[1, 2, 3, 4, 5] M = 2, N = 4
--> [1, 4, 3, 2, 5]

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7    M = 3   N = 5    ----->
1 -> 2 -> 5 -> 4 -> 4 -> 6 -> 7    


Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return 
the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:





#> Linked Lists: Merge Multi-Level Doubly-Linked List (Medium)
"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list, which contains nodes that have a next pointer,
a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list,
also containing these special nodes. These child lists may have one or more
children of their own, and so on, to produce a multilevel data structure
as shown in the example below.

Given the head of the first level of the list, flatten the list so that all
the nodes appear in a single-level, doubly linked list. Let curr be a
node with a child list. The nodes in the child list should appear after curr and
before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their
child pointers set to null.
"""

"""
How the multilevel linked list is represented in test cases:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]



# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':


#> Linked Lists: Linked List Cycle Detection (Medium)
"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next 
pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos 
is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""

## Approach 1: Naive Approach

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

## Approach 2: Floyd's Tortoise and Hare Algorithm
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:



#> Stacks: Valid Parentheses (Easy)
"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
def isValid(self, s: str) -> bool:



#> Stacks: Minimum Remove to Make Valid Parentheses (Medium)
"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""
def minRemoveToMakeValid(self, s: str) -> str:




#> Trees: Maximum Depth of Binary Tree (Easy)
"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

Maximum depth is the number of nodes along the longest path from the root node
to the furthest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


# Trees: Invert a Binary Tree (Easy)
"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:





#> Trees: Level Order Traversal of Binary Tree (Medium)
"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


#> Trees: Binary Tree Right Side View (Medium)
"""
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:






#> Full & Complete Binary Trees - Number of Nodes in Complete Tree (Medium)
"""
https://leetcode.com/problems/count-complete-tree-nodes/

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled 
in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2^h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.


Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nLayers = self.countLayers(root, 0) - 1
        nodesBeforeLastLayer = 2 ** nLayers - 1

        # Do binary search to find the last node.
        # We do it by searching if mid exists
        low = 0
        high = nodesBeforeLastLayer
        while low < high:
            indexToFind = ceil((high + low) / 2)
            if self.nodeExists(root, indexToFind, nLayers):
                low = indexToFind
            else:
                high = indexToFind - 1

        nodesInLastLevel = low + 1

        return nodesBeforeLastLayer + nodesInLastLevel

    def nodeExists(self, root, indexToFind, nLayers):
        node = root
        low = 0
        high = 2 ** nLayers - 1
        for i in range(nLayers):
            mid = ceil((low + high) / 2)
            if indexToFind >= mid:
                low = mid
                node = node.right
            else:
                high = mid - 1
                node = node.left
        return node is not None


    def countLayers(self, node, count):
        if not node:
            return count
        return self.countLayers(node.left, count + 1)


                    x                           0

            x              x                    1

        x      x        x      x                2

    x      x x    x   0  0   0   0              3
    0      1 2    3   4  5   6   7




#> Validate Binary Search Tree (Medium)
"""
https://leetcode.com/problems/validate-binary-search-tree/


Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursiveCheck(root, -math.inf, math.inf)

    def recursiveCheck(self, node, minV, maxV):
        if not node:
            return True
        if node.val > maxV or node.val < minV:
            return False
        return self.recursiveCheck(node.left, minV, node.val) and self.recursiveCheck(node.right, node.val, maxV)

#                30  betwen -inf and inf

#     -inf  20 (30)       30   50  inf

#   -inf 15 (20)    (20) 25 (30)    40   55



#> Find Mode in Binary Search Tree (Easy)
"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:





#> Graphs: Traverse Graph with BFS
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
def traversalBFS(graph): # graph has the shape of our adj list
    q = [0]
    res = []
    seen = {}

    while q:
        current = q.pop(0)
        res.append(current)
        seen[current] = True

        neighbours = graph[current]
        for n in neighbours:
            if n not in seen:
                q.append(n)
    return res


#> Graphs: Traverse Graph with DFS
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
def traversalDFS(graph): # graph has the shape of our adj list
    res = []
    seen = {}
    recursiveDFS(0, res, seen)
    return res

def recursiveDFS(node, res, seen):
    res.append(node)
    seen[node] = True
    neighbours = graph[node]
    for n in neighbours:
        if n not in seen:
            recursiveDFS(n, res, seen)

print(traversalDFS(graph))






#> Graphs: Time Needed to Inform All Employees (Medium)
"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/

A company has n employees with a unique ID for each employee from 0 to n - 1. 
The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] 
is the direct manager of the i-th employee, manager[headID] = -1. 
Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. 
He will inform his direct subordinates, and they will inform their subordinates, and so on 
until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates
(i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

**Example 1:**
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

**Example 2:**
![](2022-03-01-16-34-35.png)
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1

Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
 
Constraints:

1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0 
        adjList = self.createAdjList(n, manager, headID)
        return self.recursiveTimeLength(adjList, headID, informTime)


    def recursiveTimeLength(self, adjList, currentEmployee, informTime):
        if len(adjList[currentEmployee]) == 0:
            return 0
        managees = adjList[currentEmployee]
        return informTime[currentEmployee] + max([self.recursiveTimeLength(adjList, emp, informTime) for emp in managees])

    
    def createAdjList(self, n, manager, headID):
        adjList = [[] for i in range(n)]
        for employee, manager in enumerate(manager):
            if employee == headID:
                continue
            adjList[manager].append(employee)
        return adjList




#> Graphs: Course Scheduler (Medium)
"""
https://leetcode.com/problems/course-schedule/

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. 
You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must
take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Example 1:**

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 
**Constraints:**
```
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
```
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:




#> Graphs: Network Time Delay (Medium)
"""
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from `1` to `n`. 
You are also given times, a list of travel times as directed edges `times[i]` = `(ui, vi, wi)`,
where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal
to travel from source to target.

We will send a signal from a given node `k`. Return the time it takes for all the `n` nodes
to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Example 1:**
![](2022-03-04-10-22-30.png)
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

**Example 2:**
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

**Example 3:**
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

**Constraints:**
```
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
```
"""
class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:






#> Graphs: Network Time Delay WITH NEGATIVE WEIGHTS (Medium)
class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:











#> Dynamic Programming: Minimum Cost of Climbing Stairs (Easy)
"""
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

**Example 1:**
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

**Example 2:**
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [False for _ in cost]
        # cost[n] doesn't have an associated step, so we start without adding it, just the min between two subproblems
        return min(self.recursive(cost, len(cost) - 1, dp), self.recursive(cost, len(cost) - 2, dp))

    def recursive(self, cost, i, dp):
        if i < 0:
            return 0
        if i < 2:
            return cost[i]
        if dp[i]:
            return dp[i]

        dp[i] = cost[i] + min(self.recursive(cost, i - 1, dp), self.recursive(cost, i - 2, dp))
        return dp[i]

Time complexity: O(N)
Space complexity: O(N)

# cost[i] = 0     1       2       3       4       Fin 
#                                 n-2     n-1       n

# minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])           

#                                         minCost[n]

#                     minCost[n-1]                            minCost[n-2]
#             minCost[n-2] minCost[n-3]               minCost[n-3]       minCost[n-4]





#> Dynamic Programming: Knight Probability in Chessboard (Medium)
"""
https://leetcode.com/problems/knight-probability-in-chessboard/

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves.
The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. 
Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random
(even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

**Example 1:**
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

**Example 2:**
Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000
 
**Constraints**
1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n
"""
directions = [[1,2], [2,1], [-2, -1], [-1, -2], [1, -2], [-2, 1], [2, -1], [-1, 2]]
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[False for c in range(n)] for r in range(n)] for _ in range(k+1)]
        return self.recursiveProbability(n, k, row, column, dp)

    def recursiveProbability(self, n, k, row, column, dp):
        if row >= n or row < 0 or column >= n or column < 0:
            return 0
        if k == 0:
            return 1
        if dp[k][row][column]:
            return dp[k][row][column]
        
        prob = 0
        for x, y in directions:
            prob += self.recursiveProbability(n, k - 1, row + x, column + y, dp) / 8
        dp[k][row][column] = prob
        return prob



#> Dynamic Programming: Climbing Stairs (Easy)
"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 

**Example 1:**
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [False for i in range(n + 1)]
        return self.recursiveClimb(n, dp)
        
    def recursiveClimb(self, n, dp):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n < 0:
            return 0
        if dp[n]:
            return dp[n]
        
        dp[n] = self.recursiveClimb(n - 1, dp) + self.recursiveClimb(n - 2, dp)
        
        return dp[n]
        

#> Dynamic Programming: Fibonacci Number (Easy)
"""
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:
0 <= n <= 30
"""
class Solution:
    def fib(self, n: int) -> int:
        dp = [False for i in range(n + 1)]
        return self.recursiveFib(n, dp)
    
    def recursiveFib(self, i, dp):
        if i < 2:
            return i
        dp[i] = self.recursiveFib(i - 1, dp) + self.recursiveFib(i - 2, dp)
        return dp[i]



#> Dynamic Programming: N-th Tribonacci Number (Easy)

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [False for i in range(n + 1)]
        return self.recursiveTri(n, dp)
        
    def recursiveTri(self, i, dp):
        if i < 0:
            return 0
        if i == 0:
            return 0
        if i < 3:
            return 1
        if dp[i]:
            return dp[i]
        dp[i] = self.recursiveTri(i - 1, dp) + self.recursiveTri(i - 2, dp) + self.recursiveTri(i - 3, dp)
        
        return dp[i]
        

#> Dynamic Programming: Coin Change (Medium)
"""
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

**Example 2:**
Input: coins = [2], amount = 3
Output: -1

**Example 3:**
Input: coins = [1], amount = 0
Output: 0

**Constraints:**
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create array with max values for indexes 0 to our amount
        dp = [math.Inf for i in range(amount + 1)]
        # Our base case is 0: if amount remaining is 0, we need 0 coins
        dp[0] = 0

        # Now we compute every value in dp, starting from 1
        # until our amount
        for am in range(1, amount + 1):
            # Now we loop for every coins we have in our array
            for coin in coins:
                # We substract our current amount minus our current coin
                # If that calculation is positive (we didn't go over zero)
                # that means we can continue searching
                if am - coin >= 0:
                    # If the above check is true, we possibly found a solution
                    # or an intermediate step for our solution
                    # So we say that our current dp[amount] is the minimum between
                    # itself and (1 + dp[amount - coin])
                    # The 1 comes from the current coin that we are using
                    # The [amount - coin] comes from the fact that, for example, if the
                    # amount we had is 7, and the coin is 4, then we are saying
                    # dp[7] = 1 + dp[7 - 4] ---> One coin used (the one for the loop), plus
                    # the sub problem for the remaining amount
                    dp[am] = min(dp[am], 1 + dp[am - coin])

        # Return the last value calculated (the one we need) if it's different than
        # inifinity, otherwise return -1, because we didn't find a solution for our amount
        return dp[-1] if dp[-1] != math.inf else -1

import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.Inf for i in range(amount + 1)]
        dp[0] = 0

        for am in range(1, amount + 1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - coin])

        return dp[-1] if dp[-1] != math.inf else -1


#> Dynamic Programming: Minimum Cost For Tickets (Medium)
"""
https://leetcode.com/problems/minimum-cost-for-tickets/

You have planned some train traveling one year in advance. 
The days of the year in which you will travel are given as an integer array `days`. 
Each day is an integer from `1` to `365`.

Train tickets are sold in three different ways:

- a 1-day pass is sold for costs[0] dollars,
- a 7-day pass is sold for costs[1] dollars, and
- a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the **minimum number of dollars you need to travel every day in the given list of days.**

**Example 1:**
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

**Example 2:**
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

**Constraints:**

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
import math
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # I think this is an object and not an array, because we won't be calculating
        # the minimum cost for all days in the days array
        dp = {}
        currentDay = 0
        return self.recursiveCost(currentDay, days, costs, dp)

    def recursiveCost(self, currentDay, days, costs, dp):
        # Base case when we have reached the last day, the cost is 0. Notice that we will 
        # reach this base case, because endDay (with which the recursive function is called)
        # grows by 1 until the next travel day OR until we reach len(days). That's when will hit this base case.
        if currentDay == len(days):
            return 0
        if currentDay in dp:
            return dp[currentDay]

        dp[currentDay] = math.inf
        for travelDays, cost in list(zip([1, 7, 30], costs)):
            # First, get the index of the next day that we will need a travel pass
            endDay = currentDay
            while endDay < len(days) and days[endDay] < days[currentDay] + travelDays:
                endDay += 1
            # The cost of travelling in the current day is the minimum between what we already have calculated
            # and the cost for the current ticket (looping through 1, 7 and 30 day tickets), plus the minimum
            # cost of of travelling from my end day (so we call recursiveCost with endDay)
            dp[currentDay] = min(dp[currentDay], cost + self.recursiveCost(endDay, days, costs, dp))

        return dp[currentDay]