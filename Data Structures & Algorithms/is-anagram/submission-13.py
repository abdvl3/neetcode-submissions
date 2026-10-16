class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        anagram1,anagram2 = {},{}

        for i in range (len(s)):
            anagram1[s[i]] = 1 + anagram1.get(s[i],0)
            anagram2[t[i]] = 1 + anagram2.get(t[i],0)

        return anagram1 == anagram2

            