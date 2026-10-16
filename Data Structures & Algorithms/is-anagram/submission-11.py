class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charCount1, charCount2 = [0]*26, [0]*26

        for char in s:
            charCount1[ord(char) - ord('a')] += 1
        for char in t:
            charCount2[ord(char) - ord('a')] += 1
        
        if charCount1 == charCount2:
            return True
        else:
            return False

        