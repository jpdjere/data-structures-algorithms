def trappingRainwater(heights):
  maxLeft = maxRight = accumulatedWater = 0
  a = 0
  b = len(heights) - 1

  while a != b:

    if heights[a] <= heights[b]:
      if maxLeft > heights[a]:
        accumulatedWater += (maxLeft - heights[a])
      else:
        maxLeft = heights[a]

      a = a + 1

    else:
      if maxRight > heights[b]:
        accumulatedWater += (maxRight - heights[b])
      else:
        maxRight = heights[b]
      b = b - 1
  
  return accumulatedWater


print(trappingRainwater([1,2,3,4,5,6,4,3,6,3,5,8,7,6,3]))