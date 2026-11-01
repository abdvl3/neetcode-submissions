class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1,count2 = {},{}

        if len(s) != len(t):
            return False

        for char in range (len(s)):
            count1[s[char]] = 1 + count1.get(s[char],0)
            count2[t[char]] = 1 + count2.get(t[char],0)

        return count1 == count2