class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)
        sequences = {}
        longest = 0

        for num in nums:
            if (num-1) not in setNum:
                cur = num
                length = 0
                while cur in setNum:
                    length += 1
                    cur +=1
                longest = max(length,longest)
        
        return longest
                

