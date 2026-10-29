class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i,n in enumerate(nums):
            goal = target - n

            if goal in prevMap:
                return [prevMap[goal],i]

            prevMap[n] = i

        