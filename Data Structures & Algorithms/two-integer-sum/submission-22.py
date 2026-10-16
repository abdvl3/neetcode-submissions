class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        numbers = {}

        for i,num in enumerate(nums):
            numbers[num] = i

        for i in range (len(nums)):
            goal = target - nums[i]
            if goal in numbers and numbers[goal] != i:
                return [i, numbers[goal]]
        return []
