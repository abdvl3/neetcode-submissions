class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i,num in enumerate(nums):
            goal = target - num
            if goal in prevMap:
                return [prevMap[goal],i]
            prevMap[num] = i