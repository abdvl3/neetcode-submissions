class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s) :
            length = ''
            while s[i] != '#':
                length = length + s[i]
                i += 1
            i += 1
            res.append(s[i:i+int(length)])
            i += int(length)
        
        return res

            

