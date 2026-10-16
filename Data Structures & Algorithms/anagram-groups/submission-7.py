class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = defaultdict(list)

        for word in strs:
            charC = [0] * 26
            for char in word:
                charC[ord(char)-ord('a')] += 1
            buckets[str(charC)].append(word)
            
        return list(buckets.values())