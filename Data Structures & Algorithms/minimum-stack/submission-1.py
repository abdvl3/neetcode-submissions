class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,val:int):
        self.stack.append(val)
        self.minStack.append(min(
            self.minStack[-1] if self.minStack else val,val))
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]

    
