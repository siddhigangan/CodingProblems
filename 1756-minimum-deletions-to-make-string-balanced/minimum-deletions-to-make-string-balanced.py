class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        deletions = 0
        
        for char in s:
            # If we see 'a' and there is 'b' before it, it's an imbalance
            if stack and stack[-1] == 'b' and char == 'a':
                stack.pop()
                deletions += 1
            else:
                stack.append(char)
                
        return deletions
