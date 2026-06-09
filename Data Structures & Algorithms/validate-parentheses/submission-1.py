class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a in "{[(":
                stack.append(a)
            else:
                if a == "]" and len(stack) and stack[-1] == '[':
                    stack.pop()
                elif a == "}" and len(stack) and stack[-1] == '{':
                    stack.pop()
                elif a == ")" and len(stack) and stack[-1] == '(':
                    stack.pop()
                else :
                    return False    
            
        if len(stack) :
            return False

        return True
                