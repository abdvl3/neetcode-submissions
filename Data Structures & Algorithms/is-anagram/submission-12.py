class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram1 = {}
        anagram2 = {}
        for char in s: 
            anagram1[char] = 1 + anagram1.get(char,0)

        for char in t:
            anagram2[char] = 1 + anagram2.get(char,0)

        print(anagram1,anagram2)

        if anagram1 == anagram2:
            return True
        else:
            return False
            