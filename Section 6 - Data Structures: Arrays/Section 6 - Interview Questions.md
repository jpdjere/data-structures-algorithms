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

### Max Subarray Solution
https://www.youtube.com/watch?v=2MmGzdiKR9Y&ab_channel=BackToBackSWE