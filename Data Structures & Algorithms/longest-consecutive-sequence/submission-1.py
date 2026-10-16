class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of a sequence is a num with no lower value

        longest = 0
        setNums = set(nums)

        for num in setNums:
            if (num-1) not in setNums:
                length = 1
                while (num+length) in setNums:
                    length+=1
                longest = max(longest,length)
        
        return longest
