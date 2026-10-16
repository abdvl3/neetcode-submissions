class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range (len(nums) + 1 )]
        print (freq)

        for i in nums:
            count[i] = 1 + count.get(i,0) 

        for num,cnt in count.items():
            freq[cnt].append(num)
        print (freq)

        res = []
        for bucket in range (len(nums),0,-1):
            for num in freq[bucket]:
                res.append(num)
                if len(res) >= k:
                    return res



            

     