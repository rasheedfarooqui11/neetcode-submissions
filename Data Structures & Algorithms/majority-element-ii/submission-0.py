class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = defaultdict(int)
        for i in nums:
            res[i] +=1 
        return [i for i,j in res.items() if j > len(nums)/3]


        