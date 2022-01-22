# Reverse a linked list (input is only the head)
"""
 f  s
[1, 2, 3, 4]
"""
def reverse(head):
  # Get the two first values
  first = head
  second = first.next

  # Set the next value of our new tail to None
  first.next = None

  # Loop while we have a second
  while second:
    # Get the node following the second, for later use
    followSecond = second.next

    # KEY: Invert the direction of the node
    second.next = first

    # Move first and second markers forward
    first = second
    second = followSecond

  return first

# M, N reversals
"""
Given numbers M, N, reverse only nodes M through N of a linked list.
[1, 2, 3, 4, 5] M = 2, N = 4
--> [1, 4, 3, 2, 5]
"""

"""
  start   L         R.  end
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 
          5 -> 4 -> 3 -> null
1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7 -> null
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


# Merge Multi-Level Doubly-Linked List

def flattenDoublyLinkedList(head):
  # Start by defining a current node and looping
  currentNode = head

  while currentNode:
    # Check if the current node has a child
    child = currentNode.child
    if child:
      # Save the next node to attach the end of the sublist
      nextNode = currentNode.next
      # First update the child's prev to link to its parent
      child.prev = currentNode
      # Update the current node's next to point to its child
      currentNode.next = child
      # Clear the parent's ref to its Child
      currentNode.child = None

      # Loop again through the sublist to find the end of the list
      currentSubNode = child
      while currentSubNode.next:
        currentSubNode = currentSubNode.next

      # Once we find the end of the list, point the nextNode previous
      # to the end of the sub list. Then point the next of the end of the
      # sublist to the next node. BUT FIRST: check there is a nextNode
      if nextNode:
        nextNode.prev = currentSubNode
        currentSubNode.next = nextNode

    # Move to the next node in the linked list for the next loop iteration
    currentNode = currentNode.next

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

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        currentNode = head
        seenNodes = set()
        while currentNode not in seenNodes:
            if currentNode.next == None:
                return None
            seenNodes.add(currentNode)
            currentNode = currentNode.next
            
        return currentNode


## Approach 2: Floyd's Tortoise and Hare Algorithm
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check edge case of Head being null
        if head == None:
            return None
        tortoise = head
        hare = head
        
        while True:
            # Move each a step forward
            tortoise = tortoise.next
            hare = hare.next
            # Check if hare has reached the tail or passed it
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