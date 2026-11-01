class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0]*26

        if len(s) != len(t):
            return False

        for char in range (len(s)):
            count[ord(s[char])-ord('a')] += 1
            count[ord(t[char])-ord('a')] -= 1

        for num in count:
            if num != 0:
                return False
        return True