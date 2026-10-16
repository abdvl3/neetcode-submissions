class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        count = {}
        bucket = [[] for i in range (0,(len(nums)+1))]
        for n in nums:
            count[n] = count.get(n,0) + 1

        for n in count.keys():
            bucket[count[n]].append(n)
        
        while k > 0:
            while not bucket[-1]:
                bucket.pop()
            mode = bucket[-1].pop()
            res.append(mode)
            k -= 1
        
        return res
        