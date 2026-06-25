class Solution:
    def isBalanced(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            # You must first ensure the stack is NOT empty before reading stack[-1]
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                # If it's an unmatched closing bracket or invalid character, fail early
                return False
                
        return len(stack) == 0
