from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for i in s:
            if i in first:
                first[i] += 1
            else:
                first.update({i:0})
            

        for i in t:
            if i in second:
                second[i] += 1
            else:
                second.update({i:0})

        if first == second:
            return True
        else:
            return False