## Excercise: Reverse a string

'''
Create a function that reverses a string it gets as an input.
'''

def reverse(text):

## Excercise: Merge Sorted Arrays

def mergeSortedArrays(arr1, arr2):

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

https://leetcode.com/problems/longest-palindromic-substring/discuss/751188/Simple-Easy-to-Follow-Python


## Excercise: Maximum Subarray

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
You are given an array of positive integers where each integer represents the height of a vertical line on a chart. Find two lines which together with the x-axis formas a container that would hold the greatest amount of water. Return the area of water it would hold.

![](2021-11-23-08-24-15.png)

As you can see from the graph, we would need to return the are of the container held between the lines with height 8 and 9 (but only using height 8).

height = 8
width = 3

area = height x width = 8 x 3 = 24
'''

def containerWithGreatestArea(arr):






## Trapping Rainwater

'''
Given an array of integers representing an elevation map where the width of each bar is 1, return how much rainwater can be trapped.

[0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2] -> 8

[] -> 0

[3] -> 0

[3, 4, 3] -> 0
'''
def trappingRainwater(heights):








## Hashtables: First Recurring Character

'''
Given an array:

array = [2, 5, 1, 2, 3, 5, 1, 2, 4];

Find the first recurring character. The above array should return 2.

'''
def findFirstRecurring(nums):





## Linked Lists: Implement a Singly Linked List

class Node:

class LinkedList:
  def __init__(self):
  def append(self):
  def prepend(self):
  def traverse(self):
  def insert(self):
  def remove(self):

## Linked Lists: Reverse a Singly Linked List

class Node:

class LinkedList:
  def reverse(self):
