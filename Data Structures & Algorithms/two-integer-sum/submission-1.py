"""
@u
Input(s): arary: nums, integer: target
output(s): indicies: i, j such that nums[i] + nums[j] == target

* i!=j
* return the answer with the smaller index first 

Example(s):
1. nums=[1,9,3,8,5] target=4
output=(0,2)

- Are there multiple answers that can be returned?
- Are there cases where there's no answer that can be returned?

What must we keep track of here?

Invariant that we should keep track of?

Are numbers within nums sorted? -> No

@m
BF/
1. We use a nested for loop to iterate through nums, starting at i=0 and j=i+1, we will test every element against i to find the possible pair.
2. Should a pair be found, we can return the answer. 
3. The invariant is that before the start of every loop, we have not yet found the pair. If a pair has been found, then the loop ends.
TC: O(N^2) -> Loop through every single possible combination 
Repeating work? We are testing previous combinations again and again. Wouldn't it be easier store previous results and build our answer ontop of previous results?


Optimized/
1. Take the target and find the complement by subtracting the target against the current element. 
2. Initialize a dictionary: track, it will keep track of each element along with its index.
3. As we traverse through nums, we will calculate the complement, and check if it exists inside our dictionary, if it does, that means that we have previously seen the element before and we should return the solution.
4. The invariant here is that before the start of each loop, for every iteration i, track should map each element in nums to its index.

TC: O(N)
SC: O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in track:
                return [track[complement], i]
            else:
                track[nums[i]] = i


        