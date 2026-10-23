class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'}':'{',']':'[', ')':'('}

        for bracket in s:
            if bracket in valid:
                if stack and stack[-1] == valid[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return (not stack)
            