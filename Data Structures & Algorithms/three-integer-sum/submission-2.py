class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        print(nums)

        for k,a in enumerate(nums):
            # if your first value is +ve after sorting, no answer so break
            if a > 0:
                break
            # if the previous number is equal to k, increment k
            if k > 0 and a == nums[k-1]:
                continue

            i,j = k+1, len(nums) - 1
            while i < j:
                goal = a + nums[i] + nums[j]
                if goal > 0:
                    j -=1
                elif goal < 0:
                    i += 1
                else: 
                    res.append([a,nums[i],nums[j]])
                    i += 1
                    j -= 1
                    #duplicate handling
                    while nums[i] == nums[i-1] and i < j:
                        i += 1            
        
        return res

