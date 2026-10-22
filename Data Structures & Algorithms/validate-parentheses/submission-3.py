class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')':'(',']':'[','}':'{'}

        for bracket in s:
            # checks if closed in correct order
            if bracket in valid.keys() and stack:
                if stack[-1] != valid[bracket]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(bracket)
            
        
        return (not stack)