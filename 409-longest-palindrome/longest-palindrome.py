from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        has_odd = False
        
        for key, val in c.items():
            if val % 2 == 0:
                res += val
            else:
                res += val - 1  # Take the largest even part
                has_odd = True  # Mark that we have a leftover character available
        
        # If we found any odd count, we can place 1 character in the exact center
        if has_odd:
            res += 1
            
        return res
