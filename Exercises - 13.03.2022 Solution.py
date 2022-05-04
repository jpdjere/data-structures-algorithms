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
# area = min(height[a], height[b]) * (b - a)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        maxArea = 0
        while a < b:
            maxArea = max(maxArea, min(height[a], height[b]) * (b - a))
            if height[b] < height[a]:
                b -= 1
            else:
                a += 1
        return maxArea


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
def trappingRainwater(heights):
  maxLeft = maxRight = 0
  a = 0
  b = len(heights) - 1
  accum = 0
  while a != b:
    if heights[a] <= heights[b]:
      if heights[a] < maxLeft:
        accum += maxLeft - heights[a]
      else:
        maxLeft = heights[a]
      a += 1

#> Arrays: Best Time to Buy and Sell Stock (Easy)
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

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
        # Keep track of two variables, minPrice and maxProfit
        minPrice = math.inf
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        return 0 if maxProfit == -math.inf else maxProfit
        


#> Dynamic Programming: Coin Change (Medium)
"""
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

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
      dp = [math.inf for _ in range(amount + 1)]
      dp[0] = 0

      for am in range(1, amount + 1):
        for coin in coins:
          remainingAmount = am - coin
          if remainingAmount >= 0:
            dp[am] = min(dp[am], 1 + dp[remainingAmount])
      return dp[amount] if dp[amount] != math.inf else -1   




#> Graphs: Number of Islands (Medium)
"""
https://leetcode.com/problems/number-of-islands/

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
      if grid is None:
        return 0

      row, col = len(grid), len(grid[0])
      visited = [[False for c in range(col)] for r in range(row)]

      counter = 0
      for i in range(row):
        for j in range(col):
          if grid[i][j] == "1" and not visited[i][j]:
            counter += 1
            self.recursiveVisit(grid, visited, i, j, row, col)
            visited[i][j] = True
      return counter

    def recursiveVisit(self, grid, visited, i, j, row, col):
      if i < 0 or i >= row or j < 0 or j >= col:
        #Out of bounds
        return
      if grid[i][j] == "0" or visited[i][j]:
        return

      visited[i][j] = True
      self.recursiveVisit(grid, visited, i + 1, j, row, col)
      self.recursiveVisit(grid, visited, i - 1, j, row, col)
      self.recursiveVisit(grid, visited, i, j + 1, row, col)
      self.recursiveVisit(grid, visited, i, j - 1, row, col)



#> Linked Lists: Reverse a Singly Linked List (Easy)
"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # 1 -> 2 -> 3 -> 4 -> 5
      # h                   t
      if head is None:
        return None
      if head.next is None:
        return head
     
      first = head
      second = first.next
    
      head.next = None 

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
[1, 4, 3, 2, 5]
    2
       c
    bf
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
          # befLeft L             R   afterRight
    #  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
              #  M              N
    #  1 -> 2 -> 6 -> 5 -> 4 -> 3 -> 7 -> 8
    # befLeft.next = right
    # left.next = afterRight
    if head.next is None:
      return head
    
    counter = 1
    current = beforeCurrent = head
    while counter < left:
      counter += 1
      beforeCurrent = beforeCurrent.next
    current = beforeCurrent.next

    beforeLeft = beforeCurrent
    leftNode = current

    first = current
    second = first.next

    while counter < right:
      counter += 1
      secondNext = second.next

      second.next = first

      first = second
      second = second.next

    beforeLeft.next = first
    leftNode.next = second

    if left == 1:
      return first
    return head

    

    
    
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
        level = []
        q = [root]
        limit = len(q)
        
        while q:
            current = q.pop(0)
            level.append(current.val)
                
            
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
                
            if len(level) == limit:
                res.append(level)
                level = []
                limit = len(q)
        
        return res
        
    



#> Stacks: Valid Parentheses (Easy)
"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

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

Input: s = ")("
Output: false

Input: s = "([{}])"
Output: false
"""
class Solution:
    def isValid(self, s: str) -> bool:
      pairs = {
        "{": "}",
        "[": "]",
        "(": ")"
      }
      stack = []
      # If it is openining. add to stack
      for c in s:
        if c in pairs:
          stack.append(c)
          continue
      # If it is closing, check that we have something in the queue
        if not stack:
          return False
      # If it is closing, check if last in stack is its pair
        lastInStack = stack[-1]
        if c == pairs[lastInStack]:
          stack.pop()
        else:
          return False
      # At the end of my loop, all brackets should have closed off,
      # meaning that my stack should be empty
      return len(stack) == 0



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

Input: s = "lee(t(c)ode"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
[3]


Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""
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


  