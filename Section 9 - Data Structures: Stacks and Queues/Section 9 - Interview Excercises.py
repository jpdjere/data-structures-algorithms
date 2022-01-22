# Valid Parenthesis
"""
"" --> True

"[{[()]}]" --> True

"[{(}" --> True
"""
def validParenthesis(string):
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

# Minimum Remove to Make Valid Parentheses

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