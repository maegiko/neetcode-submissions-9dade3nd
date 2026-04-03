class Solution:
    def isValid(self, s: str) -> bool:        
        stack = []

        for char in s:
            if (char == "(" or char == "{" or char == "["):
                stack.append(char)
            else:
                if not stack:
                    return False
                stackItem = stack.pop()
                if (
                    (char == ")" and stackItem != "(") or
                    (char == '}' and stackItem != "{") or
                    (char == ']' and stackItem != "[")
                ):
                    return False

        return len(stack) == 0