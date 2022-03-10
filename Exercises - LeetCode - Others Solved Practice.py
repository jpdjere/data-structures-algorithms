#> Valid Transactions (Medium)

"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""

class Solution: 
  def invalidTransactions(self, transactions: List[str]) -> List[str]:
    invalid = []
    recorded = []
    for t in transactions:
      recorded.append(t.split(","))
    for rec in recorded:
      [name, strTime, strAmount, city] = rec
      time = int(strTime)
      amount = int(strAmount)
      if amount > 1000:
        invalid.append(",".join([name, strTime, strAmount, city]))
        continue
      invalidSet = set()
      for prev in recorded:
        [prevName, prevStrTime, prevStrAmount, prevCity] = prev
        prevTime = int(prevStrTime)
        prevAmount = int(prevStrAmount)
        if name == prevName and city != prevCity and abs(time - prevTime) <= 60:
          invalidSet.add(",".join([name, strTime, strAmount, city]))
      invalid = invalid + list(invalidSet)
    return invalid
        
    


#> Robot Bounded Circle (Medium)

"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.

"""

## Approach 1
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        switches = {
            "north": {
                "L": "west",
                "R": "east"
            },
            "south": {
                "L": "east",
                "R": "west"
            },
            "west": {
                "L": "south",
                "R": "north"
            },
            "east": {
                "L": "north",
                "R": "south"
            },
        }
        currentDirection = "north"
        yTotal = 0
        xTotal = 0
        
        for inst in instructions:
            print(currentDirection)
            if inst == "G":

                if currentDirection == "north":
                    yTotal += 1
                elif currentDirection == "south":
                    yTotal -= 1
                elif currentDirection == "east":
                    xTotal += 1
                else:
                    xTotal -= 1
            else:
                currentDirection = switches[currentDirection][inst]
        if yTotal == 0 and xTotal == 0:
            return True
        if currentDirection != "north":
            return True
        return False
    
## Approach 2

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
      x, y = 0, 0
      dx, dy = 0, 1 # North

      # From North To West, "turn Left" ==> (-dy, dx) 
      # From North To East, "turn Right" ==> (dy, -dx)
      for inst in instructions:
        if inst == "G":
          # Add the vector of the current direction to my position
          x, y = x+dx, y+dy
        if inst == "L":
          dx, dy = -dy, dx
        if inst == "R":
          dx, dy = dy, -dx
      
      # If robot reached origin after first loop, we are in a cycle
      if x == 0 and y == 0:
        return True
      # If robot ends up with direction different to north after first loop, we are in a cycle
      if (dx, dy) != (0, 1):
        return True
      return False
