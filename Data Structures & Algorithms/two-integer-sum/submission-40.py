class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevM = {}

        for i,num in enumerate(nums):
            goal = target - num
            if goal in prevM:
                return [prevM[goal], i]
            prevM[num] = i
        
        