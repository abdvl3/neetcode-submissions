class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #list with products, that i can times with nums[i] to get result
        n = len(nums)
        pref = [1]*n
        suff = [1]*n
        res = [1]*n

        pref[0] = suff [-1] = 1
        #prefix calc
        for i in range (1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
            print(pref)

        for i in range (n-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]
            print(suff)

        for i in range (n):
            res[i] = pref[i] * suff[i]

        return res


        