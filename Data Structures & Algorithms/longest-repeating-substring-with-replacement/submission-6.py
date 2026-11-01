class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        maxF = 0
        res = 0
        seen = {}
        
        for r in range (len(s)):
            seen[s[r]] = 1 + seen.get(s[r],0)
            maxF = max(maxF,seen[s[r]])

            while (r-l+1 - maxF)> k:
                seen[s[l]] -= 1
                l+=1

            res = max(res,r-l+1)

        return res


            