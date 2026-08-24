class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        marker = []
        for i in nums:
            if i in marker:
                return True
            else:
                marker.append(i)
        return False        
        