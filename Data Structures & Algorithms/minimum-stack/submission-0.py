class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        stack = self.stack
        minStack = self.minStack

        stack.append(val)
        if minStack == [] or val <= minStack[-1]:
            minStack.append(val)

    def pop(self) -> None:
        stack = self.stack
        minStack = self.minStack

        val = stack.pop()
        if minStack[-1] == val:
            minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
