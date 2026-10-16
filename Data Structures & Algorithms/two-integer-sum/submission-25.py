class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}

        for i,cur in enumerate(nums):
            diff = target - cur
            if diff in prevHash:
                return([prevHash[diff],i])
            else:
                prevHash[cur] = i

