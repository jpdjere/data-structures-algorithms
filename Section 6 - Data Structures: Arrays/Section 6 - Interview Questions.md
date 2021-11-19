## Two Sum

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

### Two Sum Solution

For explanation of the solution, see [Section 4 - How To Solve Coding Problems](./../Section%204%20-%20How%20to%20Solve%20Coding%20Problems/Section%204%20-%20How%20to%20Solve%20Coding%20Problems.md)

```ts
// Typescript
// Time Complexity: O(N)
const twoSum = (nums: number[], target: number): number[] => {
   const seen = new Map();
   for(let i = 0; i < nums.length; i++) {
     const num = nums[i];
     const complement = target - num;
     if(seen.has(complement)) {
       return [i, seen.get(complement)]
     }
     seen.set(num, i)
   }
}
```

```python
# Python
# Time Complexity: O(N)
def twoSum(nums, target):
  seen = {}
  for index, number in enumerate(nums):
    complement = target - number
    if(complement in seen):
      return [index, seen[complement]]
    seen[number] = index
```


## Maximum Subarray

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
### Max Subarray Solution
Solution from [BackToBackSWW:](https://www.youtube.com/watch?v=2MmGzdiKR9Y&ab_channel=BackToBackSWE)
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
         0  1   2  3   4  5  6   7  8
```         

When we get a question that asks us for the maxiumum of an array or a group of items, we think of dynamic programming to think of a global solution based on smaller subproblems.

THe first go-to idea, the brute force solution, is to find all the possible contiguous subarrays that the array might have find and then find which of those has a larger sum of its values. However, this will result in an O(N^2) or even O(N^3) time complexity, depending on how the algorithm is implemented.

The difference between the quadratic and and the cubic time solutions is that for each window (left and right limits), in the cubic time solution we will add all numbers in that window every single time, while in the quadratic, we will take advantage of the sum we already have and then add the new element on the last every time the window changes:

```python
# Python
# Cubic Time
def maxSubArrayCubic(nums):
  n = lens(nums)
  #  Arbitrary minimum value for Python
  max_sum = -10000

  for left in range(0, n):
    for right in range(left, n):
      # Investigate the first window
      window_sum = 0

      # Add all items in window
      for k in range(left, right + 1):
        window_sum = window_sum + nums[k]

      # Did we beat the bust sum seen so far?
      max_sum = max(max_sum, window_sum)

  return max_sum


def maxSubArrayQuadratic(nums):
  n = lens(nums)
  max_sum = -1000000

  for left in range(0,n):
    running_sum = 0
    for right in range(left, n):

      # Add the current element to the
      # previous computed value to get
      # the subarray sum
      running_sum = running_sum + nums[right]

      # Compare
      max_sum = max(max_sum, running_sum)
  
  return max_sum
```

Who can we solve this in linear time (O(N))?
In order to do that, we need to think in terms of dynamic programming and sub problems. The most important thing to discover when doing dynamic programming is "what is the subproblem?". And that is always slightly different.

In this case, let's start thinking what the sub problem is. What is the subproblem for each element of the array:

```python
         0  1   2  3   4  5  6   7  8
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```
What is the subproblem for index 3 (if I'm standindg on index 3, i.e. my right bound is on index 3)?

The subproblem for this case is: what is the max contiguous subarray I can get when standing on index 3?

And the contiguous subarrays I can get for index 3 are:
```python
         0  1   2  3   4  5  6   7  8
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                   _
                ____
            ________
        ____________
```

And the same is true for all other indeces. If we have a subarray that **ends** on index 8 (the last one in this case), what is the best subarray that we can achieve that end in that index.

So each of these cells "asks us" what is the best subarray that we can achieve with subarrays ending at each of those cells or indeces.

So the answer to the whole question is going to come out of whichever of the indices that "performs the best", i.e. whichever of those indeces which has a subarray that ends in it that has the largest value (the max sum).

The key to understanding this to understand, at each point of our iteration, what does the item "contribute", i.e. what are the choices that we have at each element.

We have two choices:

1.  We can start a new subarray at a certain item, which means that that subarray ends at itself. We would cut all our previous progress short and say: the best I can do that ends here is just myself.
2.  Continue the max subarray coming before us, with the item we are standing on.

Let's see an example: let's pretend we have a maximum subarray that ends on index 2 that is -9.

```js
          0   1   2   3   4   5   6   7   8
nums = [ -2,  1, -3,  4, -1,  2,  1, -5,  4 ]
       [    |   |-9 |   |   |   |   |   |   ]
```

Then, when we are on index 3, does its value of 4 extend the previous best we've done in terms of a maximum contiguous sub-array or does 4 cut off the progress that we had, and just take itself? These are our two choices:

```js
const startNewItem = 4; // Our new value in itself
const extendSubarrayWithNewItems = maxSubarrayAtPreviousElement + startNewItem = -9 + 4 = -5;

const bestSolutionAtCurrentIndeces = max(startNewItem, extendSubarrayWithNewItems)
                                   = max(4, -5) = 4
```

Therefore, for index 3, taking 4 (option 1, taking the element's value) is a better choice than making 4 or index 3 an extension of the best subarrays we had before us. That why we choose 4, we can do better with just the 4.

This is the essence of the problem and the two choices that we have for each element.

The key to understand here is that **when we look back at the previous element to see what was the best subarray we could get, we don't know exactly what subarray had that sum, but we know that the best we could get is the number we got there.** (in this case, for example, -9)

So, let's do this decision from every element in the array, sequentially from left to right. Because in the first element we have nothing to compare again, we just say that the best "ending" that we have at that index, is itself:

```js
          0   1   2   3   4   5   6   7   8
nums = [ -2,  1, -3,  4, -1,  2,  1, -5,  4 ]
       [ -2 | 1 |-2 | 4 | 3 | 5 | 6 | 1 | 5 ]
```

Let's code it:
```python
# Python
# Time Complexity: O(N)

def maxSubArraySumLinear(nums):
  # Default to say the best max seen so far is the first element
  max_so_far = nums[0]

  # Also default to say the best max ending at the first element
  # is the first element itself
  max_ending_here = nums[0]

  # Loop through the rest of the array (index 0 is already considered)
  for i in range(1, len(nums)):
    """
    For each element we have 2 choices:

    1. Just take the item we are standing on: nums[i]
       (which means: subarray start an end at the index)

    2. Let the item we are standing on contribute to the
       best max we have achieved ending at i - 1: max_ending_here + nums[i]
       (which means: exten the previous subarray best, whatever it was)
      
    The max of these 2 choices will be the best answer to the subproblem.
    """
    max_ending_here = max(nums[i], max_ending_here + nums[i])

    # Check if the calculated max_ending_here is greater than the global max_so_far
    max_so_far = max(max_ending_here, max_so_far)

  return max_so_far

```

## Max Subarray Problem

Same problem as before, but this time, return the start and ending indeces of the subarray as well.

```python
"""
          0   1   2   3   4   5   6   7   8
nums = [ -2,  1, -3,  4, -1,  2,  1, -5,  4 ]
       [ -2 | 1 |-2 | 4 | 3 | 5 | 6 | 1 | 5 ]
start         _       _      
"""

def maxSubarray(nums):
  max_so_far = nums[0]
  max_ending_here = nums[0]

  begin = end = 0

  # Iterate from index 1 to the end, so cut the array.
  # This is why we also need to treat our indeces as index + 1
  # when tracking begin and end (so they align with original nums array)
  for index, value in enumerate(nums[1:]):
    # Check if my current best subarray is the one I'm standing on
    # This happens when it's better to take the current value
    # than extending my previous array (Take option 1 from above)
    if value > max_ending_here + value:
      begin = end = index + 1 
    # Check a subcondition of extending the subarray: all of the cases
    # when option 2 from above is taken end here, but we need to do
    # another check, that's why the else if. And the check is:
    # Did I find a new global maximum? Notice that this happens on
    # indeces 5 and 6, but does not happen on index 4, although the
    # maxSubarray is from 3 to 6. 
    elif max_ending_here + value > max_so_far:
      end = index + 1
    
    # Do the logic as usual to find the new local max and
    # the new global max.
    max_ending_here = max(value, max_ending_here + value)
    max_so_far = max(max_so_far, max_ending_here)
  
  return [begin, end, max_so_far]

```

## Move Zeroes

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

### Move Zeroes - Solution

```python
# Time Complexity: O(N)
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeroes = 0
    other = []
    
    # Get amount of zeroes and an array with the other numbers
    for i in nums:
        if i == 0:
            zeroes = zeroes + 1
        else:
            other.append(i)
    
    # Replace the first elements until length of other
    # with the other numbers
    for i in range(0, len(other)):
        nums[i] = other[i]
    
    # Replace the reamining ones with zeroes
    for i in range(len(other), len(nums)):
        nums[i] = 0
```