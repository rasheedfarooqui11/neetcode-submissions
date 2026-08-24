class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num],index]
            seen[num] = index 
        

        