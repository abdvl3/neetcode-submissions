class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #list with products, that i can times with nums[i] to get result
        res = [1] * len(nums)
        for index,i in enumerate (nums):
            for j in range (len(res)):
                if j != index:
                    res[j] *= i
        return res


        