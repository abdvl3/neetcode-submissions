class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing = increasing with duplicates
        # index1 has to be less than index2

        num1 = 0
        num2 = (len(numbers)-1)

        while num1 < num2:
            curSum = numbers[num1] + numbers[num2]
            if curSum < target:
                num1 +=1
            if curSum > target:
                num2 -=1
            if curSum == target:
                return [(num1+1),(num2+1)]




