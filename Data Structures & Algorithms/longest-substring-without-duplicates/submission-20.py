class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subS = set()
        l = 0
        longest = 0

        for r in range (len(s)):
            if s[r] in subS:
                while s[r] in subS:
                    subS.remove(s[l])
                    l +=1
            subS.add(s[r])
            longest = max(longest, len(s[l:r+1]))
                
        return longest
