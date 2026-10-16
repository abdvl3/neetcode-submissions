class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of a sequence is a num with no lower value

        longest = 0
        setNums = set(nums)

        for num in setNums:
            length = 1
            if (num-1) not in setNums:
                while (num+1) in setNums:
                    length+=1
                    num += 1
                longest = max(longest,length)
        
        return longest
