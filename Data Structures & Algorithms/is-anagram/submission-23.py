class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1,count2 = {},{}

        if len(s) != len(t):
            return False

        for char in s:
            count1[char] = 1 + count1.get(char,0)
        
        for char in t:
            count2[char] = 1 + count2.get(char,0)

        return count1 == count2