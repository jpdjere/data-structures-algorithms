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



#> Arrays: Binary Search (Easy)
'''
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        left = 0
        right = n - 1
        while left <= right:
            mid = floor((left + right) / 2)
            
            # Check if we found our target
            if nums[mid] == target:
                return mid

            # If not, check if our found number is greater than our target
            # (Our target is -possibly- to the left of the array)
            if nums[mid] > target:
                # Then update our right to be one less than mid
                right = mid - 1
            # Then our found number is smaller than our target
            # (Our target is -possibly- to the right of the array)
            else:
                # Update our left to be one greater than mid
                left = mid + 1

        return -1



#> Arrays: Search in Rotated Sorted Array (Medium)
"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      if len(nums) == 0:
        return -1
      
      left = 0
      right = len(nums) - 1
      while left <= right:
        mid = floor((left + right) / 2)

        if nums[mid] == target:
          return mid

        # Where is our inflection point?
        # Is it to the right?
        if nums[mid] >= nums[left]:
          # Then, our inflection point is to the right of mid, the left side is normally increasing
          # Now we try to see if our target is in the left side
          if nums[left] <= target <= nums[mid]:
            right = mid - 1
          else:
            left = mid + 1
        else:
          # Our inflection point is to the left of mid, the right side is normally increasing
          if nums[mid] <= target <= nums[right]:
            left = mid + 1
          else:
            right = mid - 1

      return -1




#> Arrays: Move Zeroes (Easy)
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
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k > length:
            k = k - length
        beforeK = nums[0:length-k]
        afterK = nums[length-k:length]
        newArray = afterK + beforeK
        for i in range(0, length):
            nums[i] = newArray[i]



#> Arrays: Container with Most Water (Medium)
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




#> Arrays: Trapping Rainwater (Hard)
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
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

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
# Image/Graph/Visualization/Chart in Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/208241/Explanation-for-the-dummy-like-me.
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



  
#> Arrays: Product of Array Except Self (Medium)
'''
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
## Approach 1: Using exponentation
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = []
        product = 1
        for idx, val in enumerate(nums):
            if val == 0:
                zeroes.append(idx)
            else:
                product = product * val
        if len(zeroes) > 1:
            return [0 for i in nums]
        if len(zeroes) == 1:
            return [0 if idx not in zeroes else product for idx, _ in enumerate(nums)]
        return [int(product * (i ** -1)) for i in nums]

## Approach 2: Using left and right product arrays

# Form arrays that tell you the products of all numbers to the "left" of a number in num,
# and the products of all the number to the "right" of a number. Use that to calculate the product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = 1
        left = [1]
        for i in range(1, len(nums)):
            leftProduct = leftProduct * nums[i - 1]
            left.append(leftProduct)
        
        rightProduct = 1
        right = [1]
        for j in range(len(nums) - 2, -1, -1):
            rightProduct = rightProduct * nums[j + 1]
            right.append(rightProduct)
        right.reverse()
        
        ans = []
        for k in range(len(nums)):
            ans.append(left[k] * right[k])
        return ans

# Time Complexity O(N)  ---> Multiple simple passes over nums
# Space Complexity O(N)  ----> Build arrays left and right and ans that have size of N


#> Array: Maximum Product Subarray (Medium)
"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
# Variation of the Maximum Subarray problem using Kadenze's algorithm. 
# Notice the main difference here is that we are not only keeping a maxProduct, but also
# a minProduct, because, due to the presence of negative numbers, the minProduct can become
# the maxProduct in every iteration, if it is multipled by a negative number. (In the same way,
# the maxProduct would become the minProduct). So in every iteration, we update both of them,
# calculating the max -for maxProduct- and min -for minProduct- of the three options:
# 1. nums[i] - our current element
# 2. maxProduct * nums[i]
# 3. savedMinProduct * nums[i] - notice we have to save a temp value because minProduct is already udpated
# And then we find our max_so_far (ans), by taking the max out of max_so_far and our new maxProduct

import math
class Solution:
    def maxProduct(self, nums):
            ans = maxProduct = minProduct = nums[0]
            for i in range(1, len(nums)):
                savedMinProduct = minProduct
                minProduct = min(nums[i], maxProduct * nums[i], minProduct * nums[i])
                maxProduct = max(nums[i], maxProduct * nums[i], savedMinProduct * nums[i])
                ans = max(maxProduct, ans)
            return ans

# Time Complexity O(N)  ---> One pass
# Space Complexity O(1)  ----> Only 3 variables      


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


#> Linked Lists: Reverse a Singly Linked List

# class Node:
#   f   s
#   1 => 2 => 3 => 4 => 5

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


#> Linked Lists: M, N reversals - Reverse Linked Lists between M and N
"""
https://leetcode.com/problems/reverse-linked-list-ii/

Given numbers M, N, reverse only nodes M through N of a linked list.
[1, 2, 3, 4, 5] M = 2, N = 4
--> [1, 4, 3, 2, 5]

[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7] L = 3 and R = 5
     p    L         R    a
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 
1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7
"""
def reverseBetweenLeftRight(head, left, right):
  currentPosition = 1
  currentNode = start = head

  # Iterate until currPosition gets to L
  # Get "start" to be node at position L - 1
  while currentPosition < left:
    start = currentNode
    currentNode = currentNode.next
    currentPosition += 1

  # We know that the new tail of our reversed part
  # is my current head, or rather the node I'm 
  # standing on now. Save it for later
  first = newReversedTail = currentNode
  second = first.next
  while currentPosition >= left and currentPosition < right:
    followSecond = second.next

    second.next = first

    first = second
    second = followSecond

    currentPosition += 1

  # At the end of the loop as written above,
  # "second" will be the first Node after the
  # part of the LL that had to be reversed,
  # in this case, it is Node 6
  # "first" will be the last node of my reversed
  # string, my new tail, which is Node 5.

  # Now we have to reassemble the linked list:
  start.next = first
  newReversedTail.next = second

  # Check special case in which left is 1,
  # then the start of our LL is actually first
  if left == 1:
    return first
  return head




# Linked Lists: Flatten a Multi-Level Doubly-Linked List (Medium)
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




#> Linked Lists: Cycle Detection
"""
https://leetcode.com/problems/linked-list-cycle-ii/

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
        # Both take a single step
        tortoise = tortoise.next
        hare = hare.next

        # Check if hare has reached last node or already passed it to a None node
        if hare.next is None or hare.next.next is None:
          return None
        
        # Hare takes its second step
        hare = hare.next

        # If both are in the same node, break the cyclce
        if hare == tortoise:
          break
      
      p1 = head
      p2 = hare
      while p1 != p2:
        p1 = p1.next
        p2 = p2.next
      
      return p1


# Linked Lists: Reorder List (Medium)
"""
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # If the list is a single node or two nodes, no modifying is needed
        if head.next is None or head.next.next is None:
            return
        
        # First, go through the list and put the nodes in a stack
        current = head
        stack = []
        while current:
            stack.append(current)
            current = current.next
        
        # Calculate how many nodes are in the list
        numberOfNodes = len(stack)
        
        # Calculate what is the id of the node that will end up as the tail
        # (so we can later iterate only up to that one and set it's next to None)
        tailNumber = ceil(numberOfNodes / 2)
        
        # Iterate until (and including) number of nodes and insert the last node
        # from the stack between the current node and its next, and advance the current
        # by 1, but move forward two nodes (to ignore the one we just inserted)
        counter = 1
        newCurrent = head
        while counter <= tailNumber:
            nodeToInsert = stack.pop()
            nextNewCurrent = newCurrent.next
            newCurrent.next = nodeToInsert
            nodeToInsert.next = nextNewCurrent
            newCurrent = newCurrent.next.next
            counter += 1
        
        # Remove the next connection from the tail node
        newCurrent.next = None





#> Linked Lists: Merge Two Sorted Lists (Easy)
"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to keep a reference to the head.
        # At dummy.next we will have alwas our first node. (Notice
        # that the first assignment that we do is current.next = SOMETHING)
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                # Assign the smaller to current.next
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # If any of the lists is over, attach the remaining
        # of the remaining list to current.next (recall it is already sorted)
        if not list1 or not list2:
            current.next = list1 or list2
        
        # Return our saved reference to our head
        return dummy.next


#> Linked Lists: Merge K Sorted Lists (Hard)
"""
You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
## Approach 1: Create a list joining all nodes from all lists, sort it and
#              then create the a new linked list out of that array

# Time complexity: O(N log N) ====> Sorting an array with all nodes
# Space complexity: O(N) =====> Creating an array that holds all nodes

class Solution(object):
    def mergeKLists(self, lists):
        nodes = []
        dummy = ListNode(0)
        current = dummy
        
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        # Loop over the sorted array of all nodes and create
        # a node for each and add to the list
        for node in sorted(nodes):
            current.next = ListNode(node)
            current = current.next
        
        return dummy.next

## Approach 2: Use a priority queue instead of creating a list with
#              all nodes and then sorting it

# Time Complexity: O(N log k), where K is the number of lists, and N of nodes
#   - The cost for every popping and insertion into the prio queue is O(log K)

# Space Complexity:
#   - O(N) for creating a new linked list
#   - O(k) for the prio queue (always has max of K nodes in it).




from queue import PriorityQueue
# Need to write the __eq__ and __lt__ functions for the ListNode Objet
ListNode.__eq__ = lambda self, other: self.val == other.val
ListNode.__lt__ = lambda self, other: self.val < other.val

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        q = PriorityQueue()
        
        # Put the K heads of lists inside our prioq
        for l in lists:
            if l:
                q.put((l.val, l))
        
        # Loop while queue is not empty
        while not q.empty():
            # Get the highest prio, create a node out of it
            # and attach it to current.next. Move current.next forward
            val, node = q.get()
            current.next = ListNode(val)
            current = current.next
            # Advanced the retrieved node forward. Add it to the prio
            # queue is there actually is a node to add.
            node = node.next
            if node:
                q.put((node.val, node))
        
        return dummy.next



#> Strings: Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterMap = {}
        for i in s:
            try:
                letterMap[i] += 1
            except KeyError:
                letterMap[i] = 1
        for j in t:
            try:
                letterMap[j] -= 1
            except KeyError:
                return False
        for remaining in letterMap:
            if letterMap[remaining] != 0:
                return False
        return True

# Strings: Group Anagrams (Medium)
"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# Approach 1: Use the sorted version of the words as keys for anagramDict
#    - Time Complexity: O(N * K log K) --->  The outer loop has an complexity of N, where N is 
#                       the number of words over which we iterate. Then in the inner loop, we 
#                       sort each string of length K with time complexity O(K log K).
#    - Space Complexity: O(K * N) ---> The total information stored in our dictionary.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        
        # Loop through the strings
        for word in strs:
            sortedWord = "".join(sorted(list(word)))
            if sortedWord not in anagramDict:
                anagramDict[sortedWord] = [word]
            else:
                anagramDict[sortedWord].append(word)

        return anagramDict.values()


# Approach 2: Use the tuple representation of the words as keys for anagramDict
#    - Time Complexity: O(N * K) --->  The outer loop has an complexity of N, where N is 
#                       the number of words over which we iterate. Then in the inner loop, we 
#                       iterate over chars of strings of length K, with time complexity O(K).
#    - Space Complexity: O(K * N) ---> The total information stored in our dictionary.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        
        # Loop through the strings
        for word in strs:
            arrayRep = [0 for i in range(26)]
            for char in word:
                code = ord(char) - 97
                arrayRep[code] += 1
            tupleRep = tuple(arrayRep)
            if tupleRep in anagramDict:
                anagramDict[tupleRep].append(word)
            else:
                anagramDict[tupleRep] = [word]
            

        return anagramDict.values()
    
    
    



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
### Approach 1:
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

### Approach 2:
def isValid(self, s: str) -> bool:
  if len(string) === 0:
    return True

  opening = ["{", "[", "("]
  closing = ["}", "]", ")"]

  stack = []
  for i in string:
    if i in opening:
      stack.append(i)
      continue

    last = stack[len(stack) - 1]
    if i in closing:
      if len(stack) === 0:
        return False

      if last === opening[0] and i === closing[0]:
        stack.pop()
        continue
      if last === opening[1] and i === closing[1]:
        stack.pop()
        continue
      if last === opening[2] and i === closing[2]:
        stack.pop()
        continue

      return False

  if len(stack) === 0:
    return True
  return False


# Stacks: Minimum Remove to Make Valid Parentheses (Medium)
"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/

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
## My Approach
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
      # opened  array to keep ( that have been openeed but not close
      opened = []
      # invalid to keep index of invalid params
      invalid = []
      # Go through str.
      for idx, ch in enumerate(s):
      # 2. If opening param, add idx to opened
        if ch == "(":
          opened.append(idx)
      # 3. If closing, check if opened has something in it. If it has, pop it. If it doesn't add idx to invalid
        if ch == ")":
          if opened:
            opened.pop()
          else:
            invalid.append(idx)

      # Create a set out of the invalid indexes arrays to retrieve them in O(1)
      invalidSet = set(opened+invalid)

      # When end, reform the string without the indexes in opened and invalid
      return "".join([ch for idx, ch in enumerate(s) if idx not in invalidSet])



## Approach 1

def minRemoveToMakeValid(self, s: str) -> str:
  # Check base case of empty string
  if len(s) == 0:
      return s
  parsedStr = list(s)
  left = []
  right = []
  for idx, val in enumerate(parsedStr):
    # If opening parenthesis, we need only to
    # add to the stack the current position, as
    # we'll have to remove it later
    if val == '(':
        left.append(idx)
    if val == ')':
        # If we find a ')' but there's no previous
        # opening '(' (left is empty), add the index
        # to the left stack, marking it to be removed later
        if len(left) == 0:
            right.append(idx)
        # Instead, if there is a matching opening pair, 
        # remove that opening pair from left
        else:
            left.pop()
  # Create a new list excluding indeces from left and right and join it
  newList = [value for idx, value in enumerate(parsedStr) if idx not in (left + right)]
  return "".join(newList)



## Approach 2

def minRemoveToMakeValid(self, s: str) -> str:
  # Check base case of empty string
  if len(s) == 0:
      return s
  parsedStr = list(s)
  stack = []
  for idx, val in enumerate(parsedStr):
    # If opening parenthesis, we need only to
    # add to the stack the current position, as
    # we'll have to remove it later
    if val == '(':
        stack.append(idx)
    if val == ')':
        # If we find a ')' but there's no previous
        # opening '(' (stack is empty), replace the
        # current char for a an empty string
        if len(stack) == 0:
            parsedStr[idx] = ""
        # Instead, if there is a matching opening pair, 
        # remove that opening pair from stack
        else:
            stack.pop()
  # Create a new list excluding indeces from left and right and join it
  newList = [value for idx, value in enumerate(parsedStr) if idx not in stack]
  return "".join(newList)


#> Check if a Parentheses String Can Be Valid (Medium)

"""
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

- It is ().
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's.
For each index i of locked,

- If locked[i] is '1', you cannot change s[i].
- But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

Example 1:
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:
Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
"""

# Input: s = "))()))", locked = "010100"

# Approach 1

# The idea is to check if parentheses are balanced from left to right and from right to left.
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
      # String can only be valid if it is even - () should close with each other
      if len(s) % 2 != 0:
        return False
      
      balance = 0
      for i in range(0, len(s)):
        # Add to the balance when parenthesis is opening
        if s[i] == "(":
          balance += 1
        # Add to the balance when parenthesis is closed, but can be reversed
        elif locked[i] == "0": # It is unlocked
          balance += 1
        # Substract from balance otherwise
        elif s[i] == ")":
          balance -= 1
        if balance < 0:
          return False
      
      balance = 0
      for i in range(len(s) - 1, -1, -1):
        if s[i] == ")":
          balance +=1
        elif locked[i] == "0": # Is open
          balance += 1
        elif s[i] == "(":
          balance -=1
        if balance < 0:
          return False
      
      return True

## Approach 2
"""
We are interested in the number of brackets which are locked and cannot be modified.

First we traverse the string from left to right and check the following

1. The chars which are unlocked.
2. The chars which are locked and are open brackets.
3. The chars which are locked and are closed brackets.
4. We need to identify the number of locked brackets which are unpaired, which is equal to number of closed brackets - number of open brackets.
5. Now the only way to balance these locked, unpaired brackets is by modifying the unlocked ones. So we check if the number of unlocked > unpaired. If it is not, then balancing is not possible and we return false.

Similarly we traverse the string from right to left and check for this condition unlocked > unpaired, which is (number of open brackets - number of closed brackets) in this case.
"""
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
      if len(s) % 2 != 0:
        return False
      
      opened, closed, unlocked = 0, 0, 0
      for i in range(0, len(s)):
        if locked[i] == "0":
          unlocked += 1
        elif s[i] == "(":
          opened += 1
        elif s[i] == ")":
          closed += 1
        unbalanced = closed - opened
        if unlocked < unbalanced:
          return False
      
      opened, closed, unlocked = 0, 0, 0
      for i in range(len(s) - 1, -1, -1):
        if locked[i] == "0":
          unlocked += 1
        elif s[i] == ")":
          opened += 1
        elif s[i] == "(":
          closed += 1
        unbalanced = closed - opened
        if unlocked < unbalanced:
          return False
      
      return True
      
# Approach 3 (similar to Approach 1)
"""
The key here is treating all unlocked parentheses as "(" when going forward and
treating all unlocked parentheses as ")" when going backwards.
"""
class Solution(object):
    def canBeValid(self, s, locked):
        if len(s) % 2:  # Intuitively, odd-length s cannot be valid.
            return False

        # traverse each parenthesis forward, treat all unlocked Parentheses as'(' and check if there is ')'
        # that cannot be eliminated by previous '(', if it exists, then the input s can't be valid.
        balance = 0
        for i in range(len(s)):
            balance += 1 if s[i] == '(' or locked[i] == '0' else -1
            if balance < 0:
                return False

        # traverse each parenthesis backward, treat all unlocked Parentheses as')' and check if there is '('
        # that cannot be eliminated by previous ')', if it exists, then the input s can't be valid.
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            balance += 1 if s[i] == ')' or locked[i] == '0' else -1
            if balance < 0:
                return False

        return True

#> Strings: Palindromic Substrings (Medium)
"""
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0
        for i in range(len(s)):
            totalCount += self.getPalindromeCount(s, i, i)
            totalCount += self.getPalindromeCount(s, i, i + 1)
        return totalCount
    
    def getPalindromeCount(self, str, i, j):
        count = 0
        while i >= 0 and j < len(str) and str[i] == str[j]:
            count += 1
            i -= 1
            j += 1
        return count



#> Strings: Longest Palindromic Substring (Medium)
"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubstr = ""
        for idx, _ in enumerate(s):
            oddCandidate = self.palindromeChecker(idx, idx, s)
            if len(oddCandidate) > len(longestSubstr):
                longestSubstr = oddCandidate
            evenCandidate = self.palindromeChecker(idx, idx + 1, s)
            if len(evenCandidate) > len(longestSubstr):
                longestSubstr = evenCandidate
        return longestSubstr
    
    def palindromeChecker(self, i, j, string):
        if i < 0 or j >= len(string):
            return ""
        while i >= 0 and j < len(string) and string[i] == string[j]:
            i -= 1
            j += 1
        # Because I have moved one extra to the sides, and only then realized
        # that my current pair doesn't match, I need to adjust the indeces.
        # i moves one position inwards, and j is not included so the current j is OK
        return string[i+1:j]



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


# Trees: Same Tree (Easy)
"""
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recursiveCheck(p, q)
        
    def recursiveCheck(self, nodeP, nodeQ):
        # Base case reached end of branch
        if nodeP is None and nodeQ is None:
            return True
        # Bases cases where one exists and the other doesn't
        if nodeP is None and nodeQ is not None:
            return False
        if nodeP is not None and nodeQ is None:
            return False
        # If both exists AND are equal, check their children recursively
        if nodeP.val == nodeQ.val:
            return self.recursiveCheck(nodeP.left, nodeQ.left) and self.recursiveCheck(nodeP.right, nodeQ.right)
        # If nodes are different, one the recursive calls from the line above will return
        # undefined, which already shortcirtcuits the and statement and ends up returning false


#> Trees: Subtree of Another Tree (Easy)
"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of 
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all 
of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isMatch(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isMatch(self, tree1Root, tree2Root):
        if tree1Root is None and tree2Root is None:
            return True
        if tree1Root is None and tree2Root is not None:
            return False
        if tree1Root is not None and tree2Root is None:
            return False
        if tree1Root.val == tree2Root.val:
            if self.isMatch(tree1Root.left, tree2Root.left) and self.isMatch(tree1Root.right, tree2Root.right):
                return True
            else:
                return False


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

#> Trees: Average of Levels in Binary Tree (Easy)
"""
Given the root of a binary tree, return the average value of the nodes on
each level in the form of an array. Answers within 10-5 of the actual answer 
will be accepted.
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        counter = len(q)
        ans = []
        levelSum = 0
        levelCounter = len(q)
        
        while q:
            counter -= 1
            current = q.pop(0)
            levelSum += current.val
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
                
            if counter == 0:
                ans.append(levelSum / levelCounter)
                counter = len(q)
                levelCounter = len(q)
                levelSum = 0
        return ans

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


#> Trees: Lowest Common Ancestor of a Binary Search Tree (Easy)
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA)
of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recursive(root, p, q)
    
    def recursive(self, node, p, q):
        if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
            return node
        
        if p.val < node.val:
            return self.recursive(node.left, p, q)
        return self.recursive(node.right, p ,q)


#> Trees: Lowest Common Ancestor of a Binary Tree (Medium)
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of 
itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recursive(root, p, q)
        
    # 3, 5, 4 left = 5 right = None
    # 1, 5, 4 left = 0 
    # 0, 5, 4 left = None right = None
    
    def recursive(self, node, p, q):
        # Reached the end of the current search space without finding either p or q, 
        # therefore there is no node that satisfies a possible LCA within that search space.
        if node is None:
            return None
        
        # Found the node that has to be the LCA (the other one will be it's descendant)
        if node.val == p.val or node.val == q.val:
            return node
        
        left = self.recursive(node.left, p, q)
        right = self.recursive(node.right, p, q)
        
        # If p and q were found to the left and right of this current node, then that means
        # that this current node must be its common ancestor
        if left and right:
            return node
        
        # Else return the node which found either p or q from its subtree 
        # If the other is None (that's why we say "left or right"), then that means
        # that the other one (p or q) will be a descendant from it.
        # So this current node is the LCA. (Follow with Example 2)
        # (Notice both may be None, and this return None, like at the 
        # end of a branch where neither p or q were found)
        return left or right
        



#> Trees: Kth Smallest Element in a BST (Medium)
"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) 
of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you 
need to find the kth smallest frequently, how would you optimize?
"""
# Approach 1: Doing Inorder DFS (guarantees sorted order) and then return k-1 element of array
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      inorder = []
      self.dfs(root, inorder)
      return inorder[k - 1]
      
    def dfs(self, root, answer):
      if root.left:
        self.dfs(root.left, answer)
      answer.append(root.val)
      if root.right:
        self.dfs(root.right, answer)

# Approach 2: Iterative Inorder Traversal, with help of a stack, we don't need to build the
#             entire inorder array, we can stop after the kth element
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      stack = []
      node = root
      
      while True:
        while node:
          # Notice we are appending the root to the stack first, which seems
          # confusing, since the most leftward node in the tree should go first
          # in an inorder array. However, notice that two lines later, we are popping
          # the last element from the stack, so basically going from the last to the
          # first, esentially reversing the order in which we added them to the stack
          # and giving our algorithm the right order of elements retrieve (which is
          # from smaller to greatest).
          stack.append(node)
          node = node.left
        node = stack.pop()
        k = k - 1 # Decrease to know when we reach 0
        if k == 0:
          return node.val
        node = node.right


        
#> Trees: Construct Binary Tree from Preorder and Inorder Traversal (Medium)
"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution./32947

Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, construct and
return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder = [9,3, 15, 20, 7]
        # preorder = [3, 9, 20, 15, 7]
        return self.recursiveBuildTree(preorder, inorder)

    def recursiveBuildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        
        idxOfRootInInorder = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[idxOfRootInInorder])
        
        node.left = self.recursiveBuildTree(preorder, inorder[:idxOfRootInInorder])
        node.right = self.recursiveBuildTree(preorder, inorder[idxOfRootInInorder+1:])
        
        return node

# Note that in this problem, left subtree will be used first. This is done due to the relation 
# between inorder and preorder (as opposed to postorder and preorder in the similar exercise).



#> Intervals: Insert Interval (Medium)
"""
https://leetcode.com/problems/insert-interval/

VIDEO SOLUTION: https://www.youtube.com/watch?v=A8NUOmlwOlM

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start 
and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 
Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for idx, currentInterval in enumerate(intervals):
            newStart, newEnd = newInterval
            currentStart, currentEnd = currentInterval
            
            # newInterval is to the left of my current interval, just append the newInterval
            # and return that plus all the other interval attached to its right
            if newEnd < currentStart:
                res.append(newInterval)
                return res + intervals[idx:]
            elif newStart > currentEnd:
            # newInterval is to the right of my current interval. So just append the currentInterval
            # to the res, and simply continue, because the newInterval could stil clash with the
            # upcoming currentIntervals in the list
                res.append(currentInterval)
            else:
                # We have a clash, so the indeces need to be merged
                newIntervalStart = min(currentStart, newStart)
                newIntervalEnd = max(currentEnd, newEnd)
                newInterval = [newIntervalStart, newIntervalEnd]
        
        res.append(newInterval)
        return res


#> Intervals: Merge Intervals (Medium)
"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return 
an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        # Sort the intervals by their start and loop thorugh them
        for currentInterval in sorted(intervals):
            currentStart, currentEnd = currentInterval
            # If res is empty, just add the current array. Notice that the else case handles this
            # if in the if check of the following line we just check for res to not be empty
            # if not res:
            #     res.append(currentInterval)
            #     continue
            if res and currentStart <= res[-1][1]:
                res[-1] = [min(currentStart, res[-1][0]), max(currentEnd, res[-1][1])]
            else:
                res.append(currentInterval)
        
        return res
            
#> Intervals: Non-overlapping Intervals (Medium)
"""
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals 
you need to remove to make the rest of the intervals non-overlapping.


Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Create array where to store accepted intervals and counter to count removed
        res = []
        removed = 0
        
        # Sort by starting time and loop over intervals
        for currentInterval in sorted(intervals):
            currentStart, currentEnd = currentInterval

            # Check if res has an interval in it already AND
            # check if the current start is less than the end of the
            # last interval that we have in our res array. If that is the
            # case, then intervals are overlapping and one should be removed.
            # (Notice that [1, 2] and [2, 5] are NOT overlapping, that's why < )
            if res and currentStart < res[-1][1]:
                removed += 1
                # Once realized that they're overlapping, we need to take the decision of
                # which one to remove. It's always better to remove the one with the greater
                # end time, since it will overlap with the most amount of upcoming intervals.
                res[-1] = res[-1] if currentEnd > res[-1][1] else currentInterval
            # Else, just append the current interval.
            else:
                res.append(currentInterval)
        
        return removed
            
                








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


#> Graphs: Clone Graph (Medium)
"""
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        q = [node]
        graphMap = {}
        
        graphMap[node.val] = Node(node.val)
        
        while q:
            current = q.pop(0)
            neighbors = current.neighbors
            for n in neighbors:
                if n.val not in graphMap:
                    q.append(n)
                    graphMap[n.val] = Node(n.val)
                graphMap[current.val].neighbors.append(graphMap[n.val])
        return graphMap[node.val]








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
        adjList = self.getAdjList(n, manager)
        return self.recursiveDFS(0, headID, informTime, adjList)

    def recursiveDFS(self, totalTime, managerID, informTime, adjList):
        if len(adjList[managerID]) == 0:
            return 0
        managees = adjList[managerID]
        totalTime += informTime[managerID] + max([self.recursiveDFS(totalTime, employee, informTime, adjList) for employee in managees])
        return totalTime
    
    def getAdjList(self, n, manager):
        adjList = [[] for i in range(n)]
        for employee, man in enumerate(manager):
            if man == -1:
                continue
            adjList[man].append(employee)
        return adjList

# Time complexity: O(N)
# Space complexity: O(N)



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
      # Create an indegree array
      indegree = self.createIndegree(numCourses, prerequisites)

      # Create an adjacency list
      adjList = self.createAdjList(numCourses, prerequisites)

      # Start topological sort:
      # 1. Create a stack to keep in it the idx of the values with 0 in indegree
      stack = []
      for idx, val in enumerate(indegree):
        if val == 0:
          stack.append(idx)
      # 2. Create a counter to keep track of how many nodes we have removed from
      #    our indegree array
      counter = 0

      # Actually do topological sort
      while stack:
        counter += 1
        # Take the first node in the stack that has indegree value of 0
        current = stack.pop()
        # Look for its neighbours to adjust indegree
        neighbours = adjList[current]
        for n in neighbours:
          indegree[n] -= 1
          if indegree[n] == 0:
            stack.append(n)
      
      if counter == numCourses:
        return True
      return False

      # If at the end of topological sort, we have removed all nodes, there are no cycles
    
    def createIndegree(self, numCourses, prerequisites):
      indegree = [0 for i in range(numCourses)]
      for course, _ in prerequisites:
        indegree[course] += 1
      return indegree
    
    def createAdjList(self, numCourses, prerequisites):
      adjList = [[] for i in range(numCourses)]
      for course, prerequisite in prerequisites:
        adjList[prerequisite].append(course)
      return adjList

# Time Complexity: O(E + N^2)
# Since we loop over the edges (prerequisites) to get our indegree and adjList arrays.
# But when doing topological sort, for each node, it can have edges to all other nodes, that we
# need to check, so time complexity there is N^2

# Space Complexity: O(N^2)
# Comes out of the adjList, which has size of numCourses, 
# and each element within it can have size of numCourses - 1


#> Graphs: Course Scheduler II (Medium)
"""
https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
 
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      indegree = self.createIndegree(numCourses, prerequisites)
      adjList = self.createAdjList(numCourses, prerequisites)

      stack = []
      for idx, val in enumerate(indegree):
        if val == 0:
          stack.append(idx)

      counter = 0
      res = []

      while stack:
        counter += 1
        current = stack.pop()
        res.append(current)

        neighbours = adjList[current]
        for n in neighbours:
          indegree[n] -= 1
          if indegree[n] == 0:
            stack.append(n)
      
      if counter == numCourses:
        return res
      return []

    
    def createIndegree(self, numCourses, prerequisites):
      indegree = [0 for i in range(numCourses)]
      for course, _ in prerequisites:
        indegree[course] += 1
      return indegree
    
    def createAdjList(self, numCourses, prerequisites):
      adjList = [[] for i in range(numCourses)]
      for course, prerequisite in prerequisites:
        adjList[prerequisite].append(course)
      return adjList





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
import math
from queue import PriorityQueue
class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Create an adjList, including cost of edges
    adjList = self.createAdjList(times, n)
    # Create a costs array, where we will keep our minimum cost to get to each node
    # We know that our k - 1 array will have 0 cost, because the signal starts there
    costs = [math.inf for _ in range(n)]
    costs[k - 1] = 0

    # Apply Dijikstra to fill out the costs array

    # First we need a PrioQueue to always retrieve our node with lowest current cost
    # and we seed it with our starting node. The prio is the cost and the value is the node's index 
    q = PriorityQueue()
    q.put((0, k - 1))

    # Loop until the prioQueue is empty
    while not q.empty():
      # Greedy get the node with less cost
      prio, currentNode = q.get()
      # Get the nodes neighbours
      neighbours = adjList[currentNode]
      # Loop through them and check if we need to update their cost value
      for targetNode, cost in neighbours:
        newCost = costs[currentNode] + cost
        # If the new cost is lesser than the target's node current value, update it and add it to the prioQueue
        if newCost < costs[targetNode]:
          costs[targetNode] = newCost
          q.put((newCost, targetNode))

    # If the costs array includes an Infinity, then we cannot reach all nodes, return -1
    # Otherwise, return max(costs)
    return -1 if max(costs) == math.inf else max(costs)


  def createAdjList(self, times, n):
    adjList = [[] for _ in range(n)]
    for source, target, cost in times:
      adjList[source - 1].append([target - 1, cost])
    return adjList

# Time complexity: O(E * log N)  ---> For each node we need to reshuffle our prio queue










#> Graphs: Number of Islands (Medium)
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, col = len(grid), len(grid[0]) 
        counter = 0
        
        # Create a mirror 2d array, to keep track of visited islands
        visited = [[False for c in range(col)] for r in range(rows)]
        
        for i in range(rows):
            for j in range(col):
                # If cell is and island, which hasn't been visited before, add to coutner
                if grid[i][j] == "1" and not visited[i][j]:
                    counter += 1
                    # Then fire the recursive visits
                    self.recursiveVisit(i, j, grid, visited, rows, col)
        return counter
    
    def recursiveVisit(self, i, j, grid, visited, rows, col):
        # Check if island is out of bounds
        if i < 0 or i >= rows or j < 0 or j >= col:
            return
        # Check if cell is water or has been visited before
        if grid[i][j] == "0" or visited[i][j]:
            return
        
        # Mark the island as visited
        visited[i][j] = True
        
        # Recursive call its adjacent cells
        self.recursiveVisit(i + 1, j, grid, visited, rows, col)
        self.recursiveVisit(i - 1, j, grid, visited, rows, col)
        self.recursiveVisit(i, j + 1, grid, visited, rows, col)
        self.recursiveVisit(i, j - 1, grid, visited, rows, col)
                    
        










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