class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(s[0]=='}' or s[0]==')' or s[0]==']'):
            return False
        for i in s:
            if (i == '{' or i =='[' or i == '('):
                stack.append(i)
            elif (stack and stack[-1]=='{' and i=='}'):
                stack.pop()
            elif (stack and stack[-1]=='[' and i==']'):
                stack.pop()
            elif (stack and stack[-1]=='(' and i ==')'):
                stack.pop()
            else:
                return False
        return len(stack) == 0