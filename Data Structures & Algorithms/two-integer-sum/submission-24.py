class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i,n in enumerate(nums):
            numbers[n]=i

        print(numbers)

        for i in range (0, len(nums)-1):
            diff = target - nums[i]
            if diff in numbers.keys() and numbers[diff] != i:
                return ([i,numbers[diff]])

