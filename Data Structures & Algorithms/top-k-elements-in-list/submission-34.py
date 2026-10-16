class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k = 3 return 3 most frequent elements
        # sort elements by frequency - bucket sort

        buckets = [ [] for i in range(0,len(nums)+1) ]
        count = {}
        output = []


        for num in nums:
            count[num] = 1 + count.get(num,0)

        for num,cnt in count.items():
            buckets[cnt].append(num)

        while len(output) < k:
            if len(buckets[-1]) == 0:
                buckets.pop()
            else:
                output.append(buckets[-1].pop())

        return output
        