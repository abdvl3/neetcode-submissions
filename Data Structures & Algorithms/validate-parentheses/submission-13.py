class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedMap = {')':'(',']':'[','}':'{',}

        for bracket in s:
            if bracket in closedMap.keys():
                if stack and closedMap[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(bracket)
            
        return True if not stack else False
            

        