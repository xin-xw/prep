"""
@understand
input: Provided an array, we have to return the length of the longest consecutive sequence of elements that can be formed
output: int

example: 
nums = [1,10,30,2,6]
output: 2 -> (1, 2)

nums = [3,7,1,2,4,6,8]
output: 4 -> (1,2,3,4)

nums = [2,20,4,10,3,4,5]
output: 4 -> (2,3,4,5)

* duplicates can exist

@implement
- provided a starting point, we are to look for whether that value+1 exist inside the array; what we are really interested in is the length of consecutive numbers in that array and once we find that out, when we iterate the array, we can just piece together the current number + length of longest consecutive numbers if the start of that length is == current number + 1
- i.e.: if we know len_consecutive_nums = 3 (3,4,5), then when we find 2, we can return 4
- idea here is to avoid repetitive work, so we can scan the list once to find that length and then work retroactively? 
- how can we bridge these numbers together?

1. As we iterate nums, we will create a bucket (dictionary, key) for every value. We skip duplicated values.
2. If we encounter a value that maps to a single neighbor: bucket-1 or bucket+1, then we append the current value to the respective neighbor's list.
3. If both neighbors exists: then we append the current value to the left neighbor bucket-1, then append all the right neighbor's list to the left neighbor.
4. After every append, we must remember to reference the current value to the bucket we appended it to.


0 → [0]
3 → [3]

* Reads 2: 1 neighbor exist, append current value to right neighbor; point both 2, 3 to [3, 2]
2 → [2]
3 ─┐
2 ─┴→ [3, 2]

5 → [5]

* Reads 4, 4+1=5 and 4-1=3: 2 neighbors exist, append current value to left neighbor, then add on right neighbor's list; then reference 4, 5 to the same bucket
3 ─┐
2 ─┤
4 ─┴→ [3, 2, 4] + [5]

3 ─┐
2 ─┤
4 ─┤
5 ─┴→ [3, 2, 4, 5]

* Reads 6: 1 neighbor exist, append value to 5's list; point both 5, 6 to the same list
3 ─┐
2 ─┤
4 ─┤
5 ─┤
6 ─┴→ [3, 2, 4, 5, 6]

* Reads 1: Both neighbors exist, append current value to left neighbor, then add on right neighbor's list; point both 1 and 2 to the same bucket
0 ─┐
1 ─┴→ [0, 1] + [3, 2, 4, 5, 6]

3 ─┐
2 ─┤
4 ─┤
5 ─┤
6 ─┴→ [3, 2, 4, 5, 6, 0, 1]

0 ─┐
1 ─┤
3 ─┤
2 ─┤
4 ─┤
5 ─┤
6 ─┴→ [0, 1, 3, 2, 4, 5, 6]

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Converting to set allows us to quickly check whether a number is in a set (start of a sequence)
        # "Does this number exist anywhere in the input?"
        num_set = set(nums)
        longest = 0

        for i in range(len(nums)):
            cur = nums[i]
            if cur-1 not in num_set:
                streak = 1
                while (cur+1) in num_set:
                    cur+=1
                    streak+=1
                longest = max(longest, streak)
        return longest
        

                


