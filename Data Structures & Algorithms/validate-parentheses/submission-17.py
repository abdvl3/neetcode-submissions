class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {'}':'{',')':'(',']':'[',}
        for b in s:
            if b in closed:
                if stack and closed[b] == stack[-1]:
                    stack.pop()
                else:
                    return False  
            else:
                stack.append(b)
        return True if not stack else False
            

                
            

        