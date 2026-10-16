class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = []

        for i in range (1, len(nums)):
            prev = nums[i-1]
            prefix[i] *= prev * prefix[i-1]

        for i in range(len(nums)-2 , -1, -1):
            post = nums[i+1]
            suffix[i] *= post * suffix[i+1]

        for i in range (len(nums)):
            res.append(prefix[i]*suffix[i])
        
        return res

