class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictNum = {}
        for i,n in enumerate(nums):
            dictNum[n] = i

        for i in range (0,len(nums)-1):
            goal = target - nums[i]   
            if goal in dictNum.keys() and dictNum[goal]!=i:
                return ([i,dictNum[goal]])
        return []




