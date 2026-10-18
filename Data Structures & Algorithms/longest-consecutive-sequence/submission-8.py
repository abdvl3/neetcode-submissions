class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNum = set(nums)
        longest = 0
        for num in nums:
            # if n-1 not in seq, number is start of a seq
            if (num-1) not in setNum:
                length = 1
                while (num+1) in setNum:
                    num +=1
                    length += 1
                longest = max(length,longest)
            
        return longest
          
