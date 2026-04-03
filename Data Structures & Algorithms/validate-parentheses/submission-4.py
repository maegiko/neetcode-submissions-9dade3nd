class Solution:
    def isValid(self, s: str) -> bool:        
        stack = []

        for char in s:
            if (char == "(" or char == "{" or char == "["):
                stack.append(char);
            else:
                if not stack:
                    return False
                stackItem = stack.pop(len(stack) - 1)
                if (
                    (char == ")" and stackItem != "(") or
                    (char == '}' and stackItem != "{") or
                    (char == ']' and stackItem != "[")
                ):
                    return False;

        if (len(stack) == 0): 
            return True;
        else:
            return False;