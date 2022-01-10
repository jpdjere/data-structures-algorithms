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