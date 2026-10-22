"""
@understand
input: array: heights, heights[i] represent the height of the i-th bar
- We can choose any two bars to form a container, return the maximum amount of water a container can store.
output: int: maximum amount of water a container can store

example 1:
input: heights = [1,7,2,5,4,7,3,6]
output: res = 

- Height of this container = min(7, 6) = 6
- Width of this container = subtract indices (7-1) = 6
- Total amount of water stored = 36

* The answer is not 7 / 7 (the greatest two numbers, because the closer the indices, the less water can be stored) -> What is the trick? 
* In the ideal situation, the outermost "edges" are going to be the tallest, storing the most water. The more we move inward, the less water is stored.
* How do we know when we've identified an "edge"? -> tall wall
    * We know it's an edge, if it is greater than all the numbers on the right

@plan
1. We put pointers on the edges, left, right = 0, len(heights) - 1
2. At we scan the array, we always want to computer how much this container can hold? (area)
2a. heights = [1,7,2,5,4,7,3,6]
    2b. height[0,7] = min(6,1) = 1 <- height | width = 7 (7-0=7), 1*7 = 7
    2c. Based on whichever edge is smaller, we move the pointer correspondingly.
        * 1 is smaller, so we move left pointer -> recompute
        - Our goal is to always find a taller edge

@implement
left, right = 0, len(heights)-1
res = float('-inf')

while left < right (we dont really care about the condition where they are the same bar)
    area = min(height[left], height[right]) * (right - left)
    res = max(res, area)
    if left < right:
        left += 1
    elif right > left:
        right -= 1
    else:
        right -= 1



"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        res = float('-inf')

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] > heights[left]:
                right -= 1
            else:
                right -= 1
        
        return res
        