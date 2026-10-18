class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevNum = [1]*len(nums)
        res = [1]*len(nums)
        prev,post = 1,1

        for i in range (1,len(nums)):
            prev *= nums[i-1]
            prevNum[i] *= prev

        for i in range((len(nums)-2),-1,-1):
            post *= nums[i+1]
            res[i] *= post

        for i in range(0,len(res)):
            res[i] *= prevNum[i]

        return res
