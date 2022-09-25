class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        parentheses = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        
        if len(s) == 1:
            return False
    
        for char in s:
            if char in parentheses.values():
                stack.append(char)
                pass
             
            elif char in parentheses:
                if len(stack) < 1:
                    return False
                elif parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        
        if len(stack) == 0:
            return True
        else:
            return False
        
                
