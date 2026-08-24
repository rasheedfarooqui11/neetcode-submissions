class Solution(object):
    def majorityElement(self, nums):
        hash = defaultdict(int)
        for i in nums:
            hash[i] +=1
        return [i for i,j in hash.items() if j>(len(nums)//2)][0]

        