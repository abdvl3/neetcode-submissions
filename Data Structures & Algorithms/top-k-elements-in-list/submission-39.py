class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(0,len(nums)+1)]
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for num,freq in count.items():
            buckets[freq].append(num)

        while k > 0:
            while not buckets[-1]:
                buckets.pop()
            res.append(buckets[-1].pop())
            k -= 1
        return (res)
