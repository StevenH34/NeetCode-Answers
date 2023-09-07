"""
217. Contains Duplicate

Given an integer array nums, return true if any value 
appears at least twice in the array, and return false 
if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Time & Space: O(n) 

Other Solution:
    Sort the array then use two ptrs.
    Not as fast, but uses less space.
    Time:  O(n log n)
    Space: O(1) 
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
