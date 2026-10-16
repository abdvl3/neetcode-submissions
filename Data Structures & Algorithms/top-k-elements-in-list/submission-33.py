class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range (len(nums) + 1)]
        res = []

        countNums = {}

        for num in nums:
            countNums[num] = 1 + countNums.get(num,0)

        for num in countNums.keys():
            buckets[countNums[num]].append(num)


        for i in range (len(buckets)-1, -1, -1):
            for j in range (len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
