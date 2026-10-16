class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use ord to make strings
        anagrams = defaultdict(list)
        output = []

        for word in strs:
            countC = [0]*26

            for i in word:
                countC[ord(i)-ord('a')] += 1

            anagrams[str(countC)].append(word)

        for results in anagrams.values():
            output.append(results)
        
        return output
            

        