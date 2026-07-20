"""
U: Given an integer arr: nums, I should return T if any value appears more than once in the array, otherwise I should return False.
Examples:

Input: nums = [1,2,3,4,4]
Output: True, reasoning 4 appears more than once

Input: nums = [1,2,3,4,5]
Output: False, reasoning: all numbers are unique

Do I have to check the validity of each element in the array? -> Will there be other characters other than integers?

M: 
BF/
1. Go through nums, as we iterate across each element, have a dictionary: track that will keep track of the frequency and count
2. Because we are testing for uniqueness, if the element is already in the dictionary, then we can simply return True
3. Otherwise, we can return False

TC: O(N), SC: O(N) 

P.S.: We can also use a set and return the len(nums) and compare it against the set's length

Invariances:
1. Before the loop, 

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            cur_elt = nums[i]
            if cur_elt in seen:
                return True
            seen.add(cur_elt)
        return False