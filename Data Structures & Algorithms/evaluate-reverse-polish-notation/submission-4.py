class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        res = tokens[0]
        for t in tokens:
            if t in operators:
                val1 = int(stack.pop())
                val2 = int(stack.pop())

                if t == '+':
                    res = val1 + val2
                elif t == '-':
                    res = val2 - val1
                elif t == '*':
                    res = val1 * val2
                else:
                    res = val2 / val1
                
                stack.append(res)
            else:
                stack.append(t)
        
        return int(res)
                        