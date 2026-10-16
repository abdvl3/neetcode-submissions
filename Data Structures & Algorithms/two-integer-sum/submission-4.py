class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #index NOT values of numbers
        #smaller index value first

        needed = 0
        seen = {}

        for i in range (0, len(nums)):
            needed = target - nums[i]
            if needed in seen.keys():
                return [seen.get(needed),i]
            else:
                seen.update({nums[i]:i})