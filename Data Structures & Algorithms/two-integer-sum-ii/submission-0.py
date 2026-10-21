"""
@understand
Input: numbers (array), target (int) 
Output: array
* O(1) additional space 
* input array is sorted -> sorted input gives us a huge hint on using two pointers, right?
* TC should be less than O(nlogn)

- We are to return indices (1-indexed) of two numbers [index1, index2] such that they add up to a given target number, target. 
- index1 < index2, and they cannot be equal to one another.
- Assume that there's always one valid solution

ex1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]

@match
array, two pointers
- can't use additional space (also another huge hint to use two pointers)

@plan
* What do we know for sure and what is the invariant?
- We know for sure the target value. If we just look at the target value, we can gauge closer to the answer by moving our left pointer to the right (increase our value) or right pointer to the left (decrease our value). 
[1,2,3,4]
 l     r

1+4=5 5 > 3, decrease our right pointer by 1
1+3=4 4 > 3, decrease our right pointer by 1
1+2=3 3 = 3, answer found
- Condition remains while left < right
- not <= because there's never a case where the index should be the same

1. Two pointers: left, right
2. While left < right, sum up the value of the two pointers
2a. If the sum is less than our target -> increase our left pointer
2b. If the sum is greater than our target -> decrease our right pointer
3. If the sum is our target, return the current indices + 1


"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        




        