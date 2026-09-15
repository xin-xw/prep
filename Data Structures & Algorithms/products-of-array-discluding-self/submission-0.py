"""
@understand
input: provided array nums
output: output[i] is the product of all the elements of nums except nums[i]

example: 
nums = [1,2,3,4,5]
output = [2*3*4*5, 1*3*4*5, 1*2*4*5, 1*2*3*4] 

output[i] = (product of everything to the LEFT of i)  ×  (product of everything to the RIGHT of i)

output = [120, 60, 40, 24]

@match
brute-force

1. for loop to iterate through nums
2. helper fn aggregate(nums, pos_to_avoid) that computes the result for us
3. main for loop will pass in current position as the pos_to_avoid to helper fn, which will compute the solution for nums[i] for us
4. o(n^2): we iterate through nums loop, and for each element, we run through the for loop again

if we were to be able to use division, we could just aggregate all the product and then to divide by nums[i], but we can't

how do we get this down to o(n), what work are we repeating? -> we are calculating the multiplication of every element again and again


What if we do 2 O(n) passes: 1) to build a left array that aggregates everything on the left of i, and 2) to build a right array that aggregates everything on the right of i?

We notice a pattern:
    1. nums = [1,2,3,4,5]
       nothing left of nums[0] -> 1
       left of nums[1] -> 1
       left of nums[2] -> 2*1 -> left[i-1] * nums[i-1] 
       Take the previous result and multiply it by nums[i-1]
       left = [1,1,2*1,3*2*1,4*3*2*1]
       
       left = [1,1,2,6,24]

       right = [1*5*4*3*2,1*5*4*3,1*5*4,1*5,1]
       right[i] = right[i+1] * nums[i+1]
       right = [120,60,20,5,1]

       output = [120,60,40,30,24]

       output = left[i] * right[i]


@plan
compute our left and right fns
1. 

left_of_i = [] -> I forgot how to instantiate this to the same # of elts as nums
right_of_i = []

for i in range(len(nums)):
    left_of_i.append(1)
    right_of_i.append(1)
    

This is the long way...

for i in range(1, len(nums)):
    left_of_i[i] = left_of_i[i-1] * nums[i-1]

for i in range(len(nums)-2, 0):
    right_of_i[i] = right_of_i[i+1] * nums[i+1]

need to sort edge cases 

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_of_i = []
        right_of_i = []
        res = []

        for i in range(len(nums)):
            left_of_i.append(1)
            right_of_i.append(1)

        for i in range(1, len(nums)):
            left_of_i[i] = left_of_i[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_of_i[i] = right_of_i[i+1] * nums[i+1]


        for i in range(len(nums)):
            res.append(left_of_i[i] * right_of_i[i])

        return res


        