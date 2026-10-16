class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevHash = {}
        
        for i,n in enumerate(nums):
            goal = target - n    
            if goal in prevHash.keys():
                return [prevHash[goal],i]
            prevHash[n] = i

        return []    


