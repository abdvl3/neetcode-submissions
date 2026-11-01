class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        buckets = [[] for i in range (len(nums)+1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for num in count:
            buckets[count[num]].append(num)

        for i in range(len(nums)-1,-1,-1):
            if len(res) == k:
                return res
            while not buckets[-1]:
                buckets.pop()
            res.append(buckets[-1].pop())
        
        return res

