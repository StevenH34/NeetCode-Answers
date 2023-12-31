"""
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Solution:
    Create an empty Hash Map for our one pass solution
        value : index
    Subtract the val at index 0 from the target val
    Search HM for the difference
    If the val is not in the HM, add it
    Cont' to the next index until a difference is found or not

Time & Memory: O(n)

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index, Hash Map

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i