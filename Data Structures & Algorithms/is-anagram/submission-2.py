class Solution:
    # inital thought is a dictionary
    def isAnagram(self, s: str, t: str) -> bool:
        # fail case
        if (len(s) != len(t)):
            return False
        
        else:
            sCharCount = {}
            tCharCount = {}
            for i in range (0, len(s)):
                # 'in' keyword compares parameter to keys, not values
                if s[i] in sCharCount:
                    sCharCount[(s[i])] += 1
                else:
                    # .update() to add to dictionary
                    sCharCount.update({s[i] : 1})

                if t[i] in tCharCount:
                    tCharCount[(t[i])] += 1
                else:
                    # .update to add to dictionary
                    tCharCount.update({t[i] : 1})
        
        #compare dictionaries used to count characters
            if (tCharCount == sCharCount):
                return True
            else:
                return False

