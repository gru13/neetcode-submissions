class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a in "[({":
                stack.append(a)
                continue
            if len(stack) == 0:
                return False
            if a == ")" and stack[-1] != "(":
                return False
            if a == "}" and stack[-1] != "{":
                return False
            if a == "]" and  stack[-1] != "[":
                return False
            stack.pop()

        return len(stack) == 0