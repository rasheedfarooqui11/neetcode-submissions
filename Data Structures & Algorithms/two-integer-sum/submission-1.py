class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i,val in enumerate(nums):
            check = target-val
            if check in nums:
                j = nums.index(check)
                if i != j:
                     return [i, j] if i < j else [j, i]
        