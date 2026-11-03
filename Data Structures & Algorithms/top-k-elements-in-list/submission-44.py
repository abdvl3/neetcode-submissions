class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        buckets = [[]for i in range(len(nums)+1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num,0)

        for num,freq in count.items():
            buckets[freq].append(num)

        while len(res) < k:
            while not buckets[-1]:
                buckets.pop()
            
            cur = buckets[-1].pop()
            res.append(cur)

        return res


        


