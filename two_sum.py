# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j in range((i+1), len(nums)):
                if (num + nums[j]) == target:
                    return [i,j]
        

# [0, 1, 2, 3, 4]
# 0,1 ; 0,2 ; 0,3 ; 0,4
# 1,2 ; 1,3 ; 1,4 
# 2,3 ; 2,4
# 3,4
# Dont need to check last index
# index, index + 1, up to length of list