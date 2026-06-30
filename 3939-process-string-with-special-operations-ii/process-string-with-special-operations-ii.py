class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        
        # Pass 1: Calculate the final virtual length of the string
        for char in s:
            if char.isalpha():
                length += 1
            elif char == '*':
                length = max(0, length - 1)
            elif char == '#':
                length *= 2
            else:  
                length = length 
                
        # If the requested index k is out of the bounds of the final string length
        if k >= length or k < 0:
            return '.'
            
        # Pass 2: Work backward from the end of s to trace index k
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            
            if char.isalpha():
                # If k hits the very last position of the current virtual string, this is our char!
                if k == length - 1:
                    return char
                length -= 1
                
            elif char == '*':
                length += 1
                
            elif char == '#':
                # Since the string was duplicated (res += res), the index wraps around 
                # into the first half if it falls in the second half.
                half = length // 2
                if k >= half:
                    k -= half
                length = half
                
            else:
                k = length - 1 - k
                
        return '.'
