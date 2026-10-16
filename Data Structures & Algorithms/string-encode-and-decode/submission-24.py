class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res = res + str((len(word))) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:

        left,right = 0,0
        res = []

        while right < len(s):
            left = right
            while s[right] != '#':
                right += 1
            # when this while loop ends, should be on a hashtag
            length = int(s[left:right])
            right += 1
            left = right
            right += length
            res.append(s[left:right])

        return res

