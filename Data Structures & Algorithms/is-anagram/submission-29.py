class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1,count2 = {},{}

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            count1[s[c]] = count1.get(s[c],0) + 1
            count2[t[c]] = count2.get(t[c],0) + 1
        
        return count1 == count2
            