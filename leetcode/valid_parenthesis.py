
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = list()
        
        
        
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                try:
                    expected = stack.pop()
                except Exception:
                    return False
                
                if expected == '(' and c!= ')':
                    return False
                
                if expected == '[' and c!= ']':
                    return False
                
                if expected == '{' and c!= '}':
                    return False
                
        if len(stack) == 0:
            return True
        return False