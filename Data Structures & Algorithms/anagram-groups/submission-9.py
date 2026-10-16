class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted = defaultdict(list)

        for word in strs:
            count = [0]*26

            for char in word:
                count[ord(char) - ord('a')] +=1
            
            sorted[str(count)].append(word)

        return list(sorted.values())

        

                    