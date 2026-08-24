
class Solution(object):
    def topKFrequent(self, nums, k):
        hash = defaultdict(int)
        for i in nums:
            hash[i] += 1
        sorted_hash = dict(sorted(hash.items(), key = lambda x: x[1], reverse = True))
        return [ value for index,value in enumerate(sorted_hash.keys()) if index < k]
        