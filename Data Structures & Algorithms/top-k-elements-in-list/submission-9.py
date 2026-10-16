class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return k number of elements from top to bottom of modal elements.

        modeN = {}
        buckets = [[] for i in range (0,(len(nums) + 1))]
        res = []

        for num in nums:
            modeN[num] = 1 + modeN.get(num,0)

        for num,freq in modeN.items():
            buckets[freq].append(num)

        for i in range (len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                


            
        

