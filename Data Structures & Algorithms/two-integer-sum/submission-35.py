class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i in range (len(nums)):
            goal = target - nums[i]

            if goal in prevMap:
                return [prevMap[goal],i]

            prevMap[nums[i]] = i

        
        