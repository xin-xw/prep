"""
@understand
input: nums = [2,20,4,10,3,4,5]
output = 4 (2,3,4,5)

* input can contain duplicates
* input is not sorted

@match
q: as we iterate through list, we need to find and check if neighbors exist -> tells us start of sequence
* 2-1 (no left neighbor), 2+1 (yes right neighbor) -> start of sequence
- set, dictionary for O(1) neighbor look-ups

@plan
- after we find the start of sequence (no left, yes right neighbor), we can continue iterating the value of starting sequence until it does not exist in our set/dictionary
- document the max value 
- do this for every starting sequence; skip numbers that have no neighbors or have both neighbors
- ignore duplicates (will cause algo. to restart)

@implement
1. num_set = set(nums)
2. for num in num_set:
    check if it is a starting sequence (no left neighbor)
        if num is starting sequence, streak = 1, cur = num
        while cur+1 in num_set:
            cur+=1
            streak+=1
        record max streak

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num-1 not in num_set:
                strk, cur = 1, num
                while cur+1 in num_set:
                    strk+=1
                    cur+=1
                ans = max(ans, strk)
        return ans