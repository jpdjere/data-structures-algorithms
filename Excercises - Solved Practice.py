## Excercise: Reverse a string

'''
Create a function that reverses a string it gets as an input.
'''

def reverse(text):
  return text[::-1]

## Excercise: Merge Sorted Arrays

def mergeSortedArrays(arr1, arr2):
  i = j = 0
  sortedArray = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      sortedArray.append(arr1[i])
      i += 1
    else:
      sortedArray.append(arr2[j])
      j += 1
  
  while i < len(arr1):
    sortedArray.append(arr1[i])
    i += 1

  while j < len(arr2):
    sortedArray.append(arr2[j])
    j += 1

  return sortedArray

print(mergeSortedArrays([1,4,5,7,9,11], [2,3,4,8,9]))



## Excercise: Two Sum

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
  for idx, num in enumerate(arr):
    complement = target - num
    if complement in seen:
      return [seen[complement], idx]
    seen[num] = idx
  return "Not found"


  
## Excercise: Longest Palindromic Substring

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



## Excercise: Maximum Subarray

'''
Given an integer array `nums`, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

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
  max_so_far = nums[0]
  max_ending_here = nums[0]

  for i in range(1, len(nums)):
    max_ending_here = max(nums[i], max_ending_here + nums[i])
    max_so_far = max(max_so_far, max_ending_here)

  return max_so_far


def maxSubarray(nums):
  max_so_far = max_ending_here = nums[0]

  for i in range(1, len(nums)):
    max_ending_here = max(nums[i], max_ending_here + nums[i])
    max_so_far = max(max_ending_here, max_so_far)

  return max_so_far

## Excercise: Maximum Subarray with return of indeces
def maxSubArray(nums):
  max_so_far = max_ending_here = nums[0]
  begin = end = 0

  for idx, value in enumerate(nums[1:]):
    # Am I'm starting a new max subarray at this position?
    if value > max_ending_here + value:
      begin = end = index + 1
    # Did I find a new global maximum?
    elif max_ending_here + value > max_so_far:
      end = index + 1

    max_ending_here = max(value, max_ending_here + value)
    max_so_far = max(max_ending_here, max_so_far)

  return [begin, end, max_so_far] 


def maxSubarray(nums):
  max_so_far = max_ending_here = nums[0]
  begin = end = 0

  for index, value in enumerate(nums[1:]):
    # Did I find a new starting position?
    if value > max_ending_here + value:
      begin = end = index + 1
    # Did I find a new global maximum?
    elif max_ending_here + value > max_so_far:
      end = index + 1

    max_ending_here = max(max_ending_here + value, value)
    max_so_far = max(max_so_far, max_ending_here)

  return [begin, end, max_so_far]

def maxSubarray(nums):
  max_ending_here = max_so_far = nums[0]
  begin = end = 0

  for idx, val in enumerate(nums[1:]):
    # Did I find a new beginning for maxSubArray?
    if val > max_ending_here + val:
      begin = end = idx + 1
    # Did I find a new global maximum?
    elif max_ending_here + val > max_so_far:
      end = idx + 1

    max_ending_here = max(val, max_ending_here + val)
    max_so_far = max(max_so_far, max_ending_here)

  return [begin, end, max_so_far]

## Excercise: Move Zeroes

'''
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




### Excercise: Rotate Array (Medium)

'''
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


## Excercise: Container with Most Water

'''
You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
Find two lines which together with the x-axis forms a container that would hold the greatest amount of water. 
Return the area of water it would hold.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
'''

[1,8,6,2,5,4,8,3,7]
 a               b

area = (b - a) * min(arr[a], arr[b])

def containerWithGreatestArea(arr):
  length = len(arr)
  if length === 0 or length === 1:
    return 0
  
  maxArea = 0
  for a in range(0, len(arr)):
    for b in range(a + 1, len(arr)):
      newArea = (b - a) * min(arr[a], arr[b])
      maxArea = max(newArea, maxArea)
  return maxArea


def containerWithGreatestArea(arr):
  length = len(arr)
  if length == 0 or length == 1:
    return 0

  a = 0
  b = length - 1
  maxArea = 0
  while a != b:
    newArea = (b - a) * min(arr[a], arr[b])
    maxArea = max(maxArea, newArea)
    if arr[b] > arr[a]:
      a += 1
    else:
      b -= 1
  return maxArea

def containerWithGreatestArea(arr):
  length = len(arr)
  if length <= 1:
    return 0

  a = 0
  b = length - 1
  maxArea = 0

  while a != b:
    newArea = (b - a) * min(arr[a], arr[b])
    maxArea = max(newArea, maxArea)
    if arr[a] < arr[b]:
      a += 1
    else:
      b -= 1
  
  return maxArea


## Trapping Rainwater

'''
Given an array of integers representing an elevation map where the width of each bar is 1, return how much rainwater can be trapped.

[0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2] -> 8
       a           b   

[5, 4, 0, 2, 1, 0, 3] -> 
 a                 b   

[] -> 0

[3] -> 0

[3, 4, 3] -> 0
'''

"""
Brute force solution
"""

Amount of water trapped at each position = min(maxLeft, maxRight) - height at current position
def trappingRainwater(heights):
  length = len(heights)
  if length <= 2:
    return 0

  trappedWater = 0

  for i in range(0, length):
    left = heights[0:i]
    maxLeft = max(left) if len(left) > 0 else 0

    right = heights[i+1:]
    maxRight = max(right) if len(right) > 0 else 0

    calculatedWater = min(maxLeft, maxRight) - heights[i]
    if calculatedWater > 0:
      trappedWater += calculatedWater
  
  return trappedWater



accWaterOnI = min(maxLeft, maxRight) - height
def trappingRainwater(heights):
  a = 0
  b = len(heights) - 1
  trappedWater = 0
  maxLeft = maxRight = 0

  while a != b:
    if heights[a] <= heights[b]:
      if heights[a] < maxLeft:
        trappedWater += maxLeft - heights[a]
        # Missing check if trappedWater is greater than 0
      else:
        maxLeft = heights[a]
      a += 1
    else:
      if heights[b] < maxRight:
        trappedWater += maxRight - heights[b]
        # Missing check if trappedWater is greater than 0
      else:
        maxRight = heights[b]
      b -= 1
  
  return trappedWater
  


waterOnElementI = min(maxLeft, maxRight) - height
def trappingRainwater(heights):
  length = len(heights)
  if length <= 2:
    return 0

  a = 0
  b = length - 1
  trappedWater = maxLeft = maxRight = 0

  while a != b:
    if heights[a] < heights[b]:
      if heights[a] < maxLeft:
        water = maxLeft - heights[a]
        if water > 0:
          trappedWater += water
      else:
        maxLeft = heights[a]
      a += 1
    else:
      if heights[b] < maxRight:
        water += maxRight - heights[b]
        if water > 0:
          trappedWater += water
      else:
        maxRight = heights[b]
      b -= 1
  return trappedWater


  




## Hashtables: First Recurring Character

'''
Given an array:

array = [2, 5, 1, 2, 3, 5, 1, 2, 4];

Find the first recurring character. The above array should return 2.

'''
def findFirstRecurring(nums):





## Linked Lists: Implement a Singly Linked List

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __repr__(self):
    data = []
    node = self.head
    while node:
      data.append(str(node.data))
      node = node.next
    return " -> ".join(data) + "   - Head: " + str(self.head.data) + "  - Tail: " + str(self.tail.data) + " - Length: " + str(self.length)

  def append(self, data):
    newNode = Node(data)
    if self.length == 0:
      self.head = self.tail = newNode
      self.length += 1
      return self
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1
    return self


  def prepend(self, data):
    newNode = Node(data)
    if self.length == 0:
      self.head = self.tail = newNode
      self.length += 1
      return
    newNode.next = self.head
    self.head = newNode
    self.length += 1
    return


  def traverse(self, index):
    counter = 0
    node = self.head
    while counter < index:
      node = node.next
      counter += 1
    return node

  def insert(self, position, data):
    if position > self.length:
      return "Insert out of bounds"
    if position == 0:
      self.prepend(data)
      return self
    prevToNewNode = self.traverse(position - 1)
    newNode = Node(data)
    newNode.next = prevToNewNode.next
    prevToNewNode.next = newNode
    self.length += 1
    return self

  def remove(self, position):
    if position >= self.length:
      return "Remove out of bounds"
    if self.length == 1:
      self.head = self.tail = None
      self.length -= 1
      return "Empty linked list"
    if position == 0:
      self.head = self.head.next
      self.length -= 1
      if self.length == 1:
        self.tail = self.head
      return self
    prevToRemove = self.traverse(position - 1)
    prevToRemove.next = prevToRemove.next.next
    return self


## Linked Lists: Reverse a Singly Linked List

class Node:
  f   s
  1 => 2 => 3 => 4 => 5

class LinkedList:
  def revert(self):
    first = self.head
    second = first.next

    self.tail = first
    self.tail.next = None

    while second:
      followSecond = second.next
      second.next = first

      first = second
      second = followSecond

    # At the end of the loop there's no second
    self.head = first

    return self


  def revert(self):
    first = self.head
    second = first.next

    self.tail = self.head
    self.tail.next = None

    while second:
      afterSecond = second.next

      second.next = first

      first = second
      second = afterSecond

    self.head = first
    return self


# M, N reversals
"""
Given numbers M, N, reverse only nodes M through N of a linked list.
[1, 2, 3, 4, 5] M = 2, N = 4
--> [1, 4, 3, 2, 5]

[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7] L = 3 and R = 5
     p    L         R    a
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 
1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7
"""
def reverseBetweenLeftRight(head, left, right):
  counter = 1
  currentItem = previousLeft = head
  while counter < left:
    previousLeft = currentItem
    currentItem = currentItem.next
    counter += 1

  first = startOfReversedPart = currentItem
  second = first.next
  while counter >= left and counter <= right:
    afterSecond = second.next

    second.next = first

    first = second
    second = afterSecond
  
    counter += 1

  beginOfReversedPart = first
  afterRight = second

  previousLeft.next = beginOfReversedPart
  startOfReversedPart.next = afterRight

  if left == 1:
    return beginOfReversedPart
  return head










# Linked Lists: Merge Multi-Level Doubly-Linked List
"""
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

  
1---NULL
|
7---8---9---10--NULL
    |
    11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together, we will add nulls in each level to signify no node 
connects to the upper node of the previous level. The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""
def flattenDoublyLinkedList(head):
  current = head
  while current:
    if current.child:
      child = current.child
      nextToAttach = current.next
      current.next = child
      child.prev = current
      current.child = None

      currentSubNode = child
      while currentSubNode.next:
        currentSubNode = currentSubNode.next
      currentSubNode.next = nextToAttach
      if nextToAttach:
        nextToAttach.prev = currentSubNode
    current = current.next
  return head


# Linked List Cycle Detection

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
"""

## Approach 1: Naive Approach
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if head == None or head.next == None:
    return None
  current = head
  seenNodes = set()
  while current:
    if current in seenNodes:
      return current
    seenNodes.add(current)
    current = current.next
  return None
      


## Approach 2: Floyd's Tortoise and Hare Algorithm
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None or head.next == None:
        return None

      hare = tortoise = head

      while True:
        tortoise = tortoise.next
        hare = hare.next

        if hare == None or hare.next == None:
          return None
        else:
          hare = hare.next

        if hare == tortoise:
          break
      
      p1 = head
      p2 = hare
      while p1 != p2:
        p1 = p1.next
        p2 = p2.next
      
      return p1




# Stacks: Valid Parentheses (Easy)

"""
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



# Stacks: Minimum Remove to Make Valid Parentheses (Medium)
"""
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