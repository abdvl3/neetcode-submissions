from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # length#wordlength#word...
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            # 1) read length
            length = 0
            while i < n and s[i].isdigit():
                length = length * 10 + (ord(s[i]) - 48)
                i += 1

            # 2) skip '#'
            # (Assumes well-formed input like "3#cat")
            if i < n and s[i] == '#':
                i += 1
            else:
                # malformed input; break or raise
                break

            # 3) read word of 'length' chars
            word = s[i:i+length]
            res.append(word)
            i += length

        return res
