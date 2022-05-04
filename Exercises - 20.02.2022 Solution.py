#> Strings: Reverse a string

'''
Create a function that reverses a string it gets as an input.
'''

def reverse(text):
    return "".join(list(text)[::-1])



#> Arrays: Merge Sorted Arrays

arr1 = [3,4,6,7,9,9,9,20]
arr2 = [1,2,5,6,21]
def mergeSortedArrays(arr1, arr2):
  i = j = 0

  len1 = len(arr1)
  len2 = len(arr2)

  res = []

  while i < len1 and j < len2:
    if arr1[i] <= arr2[j]:
      res.append(arr1[i])
      i += 1
    else:
      res.append(arr2[j])
      j += 1

  while j < len2:
    res.append(arr2[j])
    j += 1

  while i < len1:
    res.append(arr1[i])
    i += 1

  return res

print(mergeSortedArrays(arr1, arr2))



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
  seen = {}
  for idx, val in enumerate(arr):
    complement = target - val
    if complement in seen:
      return [seen[complement], idx]
    else:
      seen[val] = idx
  return False

print(twoSum([2, 7, 11, 15], 9))


  
#> Excercise: Longest Palindromic Substring

'''
https://leetcode.com/problems/longest-palindromic-substring/discuss/751188/Simple-Easy-to-Follow-Python
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

'''

def maxSubArray(nums):
  max_so_far = max_ending_here = nums[0]

  for i in range(1, len(nums)):
    max_ending_here = max(max_ending_here + nums[i], nums[i])
    max_so_far = max(max_so_far, max_ending_here)

  return max_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

def maxSubArray(nums):
  start = end = 0
  max_so_far = max_ending_here = nums[0]

  for i in range(1, len(nums)):
    # Two things might happen on each element:
    # Did I find a new beginning for maxSubArray?
    if nums[i] > max_ending_here + nums[i]:
      start = end = i
    # Else: did I find a new global maximum?
    elif max_ending_here + nums[i] > max_so_far:
      end = i
    
    max_ending_here = max(max_ending_here + nums[i], nums[i])
    max_so_far = max(max_so_far, max_ending_here)

  return [start, end, max_so_far]

nums = [5,4,-1,7,8]
print(maxSubArray(nums))




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
  nonZero = []
  for i in nums:
    if i != 0:
      nonZero.append(i)
  
  for j in range(0,len(nonZero)):
    nums[j] = nonZero[j]

  for k in range(len(nonZero), len(nums)):
    nums[k] = 0

  print(nums)

# nums = [0,1,0,3,12]
nums = [-5,3,0 ,0,0,0,3,4,5,6,0,3,0]
moveZeroes(nums)



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

# area = min(a,b) * (b - a)
def containerWithGreatestArea(arr):
  a = 0
  b = len(arr) - 1
  maxArea = 0
  while a != b:
    area = min(arr[a], arr[b]) * (b - a)
    if area > maxArea:
      maxArea = area
    if arr[a] <= arr[b]:
      a += 1
    else:
      b -= 1
  return maxArea

nums = [1,8,6,2,5,4,8,3,7]
print(containerWithGreatestArea(nums))






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

# water on current element = max(maxHeightLeft, maxHeightRight) - currentHeight
def trappingRainwater(heights):
    a = 0
    b = len(heights) - 1
    maxLeft = maxRight = 0
    trappedWater = 0
    while a != b:
        if heights[a] < heights[b]:
            # If our current height is less than the maxLeft, we have
            # a wall to our left, that allows us to accumulate water
            if heights[a] < maxLeft:
                water = max(maxLeft, maxRight) - heights[a]
                trappedWater += water if water > 0 else 0
            else:
                maxLeft = heights[a]
            a += 1
        else:
            if heights[b] < maxRight:
                water = max(maxLeft, maxRight) - heights[b]
                trappedWater += water if water > 0 else 0
            else:
                maxRight = heights[b]
            b -= 1
    return trappedWater

nums = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(trappingRainwater(nums))





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



#> Hashtables: First Recurring Character

'''
Given an array:

array = [2, 5, 1, 2, 3, 5, 1, 2, 4];

Find the first recurring character. The above array should return 2.

'''
def findFirstRecurring(nums):
  seen = {}
  for i in nums:
    if i not in seen:
      seen[i] = True
    else:
      return i
  return False


# nums = [2, 5, 1, 2, 3, 5, 1, 2, 4]
nums = [1,2,3,4,5,6,7]
print(findFirstRecurring(nums))





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

### Full Version
class LinkedList:
  def reverse(self):
    self.head.next = None
    self.tail = self.head

    first = self.head
    second = first.next

    # Loop until there's no next to current
    # which means, first is my last node
    while second:
      secondNext = second.next

      second.next = first
      
      first = second
      second = secondNext

    self.head = first

### Leetcode Version
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        first = head
        second = first.next
        
        head.next = None

        # Loop until there's no next to current
        # which means, first is my last node
        while second:
            secondNext = second.next

            second.next = first

            first = second
            second = secondNext

        return first

#> Linked Lists: M, N reversals (Reverse Linked List II) (Medium)
"""
https://leetcode.com/problems/reverse-linked-list-ii/

Given numbers M, N, reverse only nodes M through N of a linked list.
[1, 2, 3, 4, 5] M = 2, N = 4
--> [1, 4, 3, 2, 5]
     p    L         R    a
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 
1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7

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
      if head is None:
        return None

      if head.next is None:
        return head

      counter = 1
      currentNode = prev = head

      while counter < left:
        prev = currentNode
        currentNode = currentNode.next
        counter += 1


      first = initialLeft = currentNode
      second = first.next

      while counter < right:
        secondNext = second.next

        second.next = first

        first = second
        second = secondNext

        counter += 1
        
      initialRight = first
      after = second

      prev.next = initialRight
      initialLeft.next = after

      if left == 1:
        return initialRight
      return head





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
        current = head
        while current is not None:
            if current.child is not None:
                child = current.child
                child.prev = current
                nextToParent = current.next
                current.next = child
                current.child = None

                currentSubNode = child
                while currentSubNode:
                  currentSubNode = currentSubNode.next

                if nextToParent:
                  currentSubNode.next = nextToParent
                  nextToParent.prev = currentSubNode

            current = current.next
      
        return head


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
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next == None:
            return None
        
        slow = fast = head
        
        while True:
            slow = slow.next
            fast = fast.next
            if fast.next == None or fast.next.next == None:
                return None
            fast = fast.next
            
            if fast == slow:
                break
                
        p1 = head
        p2 = fast
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1



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
  symbols = {
    "{": "}",
    "(": ")",
    "[": "]",
  }

  stack = []
  for i in s:
    if i in symbols:
      stack.append(i)
      continue

    lastInStack = stack[len(stack) - 1]
    if i == symbols[lastInStack]:
      stack.pop()
    else:
      return False
  
  return True

st = "(){}{(})}"
print(isValid(st))


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
  strList = list(s)
  stack = []
  for idx, char in enumerate(strList):
    if char == ")" and not stack:
      strList[idx] = ""
    elif char == ")":
      stack.pop()
    elif char == "(":
      stack.append(idx)

  return "".join([c for idx, c in enumerate(strList) if idx not in stack ])


"lee(t(c)o)de)"

"a)b(c)(d"

"a()b"

"))(("




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
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursiveDepth(root, 0)
    def recursiveDepth(self, node, count):
        if node is None:
            return count
        count += 1
        return max(self.recursiveDepth(node.left, count), self.recursiveDepth(node.right, count))


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
        self.recursiveInvert(root)
        return root
     
    def recursiveInvert(self, node):
        if node is None:
            return
        
        node.left, node.right = node.right, node.left
        self.recursiveInvert(node.left)
        self.recursiveInvert(node.right)





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
      if root == None:
        return []
    
      res = []
      levelNodes = []
      q = [root]
      counter = len(q)
    
      while len(q) > 0:
        counter -= 1
        current = q.pop(0)
        levelNodes.append(current.val)
        
        if current.left:
            q.append(current.left)     
        if current.right:
            q.append(current.right)
        
        if counter == 0:
            res.append(levelNodes)
            levelNodes = []
            counter = len(q)
            
      return res


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
        if root == None:
            return []
        res = []
        q = [root]
        levelNodes = []
        counter = len(q)
        
        while len(q) > 0:
            counter -= 1
            current = q.pop(0)
            levelNodes.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            
            if counter == 0:
                res.append(levelNodes.pop())
                levelNodes = []
                counter = len(q)
        
        return res
            



#> Full & Complete Binary Trees - Number of Nodes in Complete Tree (Medium)
"""
https://leetcode.com/problems/count-complete-tree-nodes/

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled 
in a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

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
    def countLevels(self, node, count):




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
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: