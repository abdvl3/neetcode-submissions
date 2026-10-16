class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need list of dictionaries, compare current word with list of dictionaries
        # if not in the list of dictionaries, add it, if it is, group it

        anagrams = {}
        for word in strs:
            cur = [0]*26

            for i in word:
                cur[ord(i) - ord('a')] +=1 #uses ord to count letters, avoids using dict

            cur = str(cur)
            if cur in anagrams:
                anagrams[cur].append(word)
            else:
                anagrams.update({cur:[word]})
        res = list(anagrams.values())
        return res

        