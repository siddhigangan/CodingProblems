class Solution:
    def processStr(self, s: str) -> str:
        res = []  
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isalpha():
                res.append(char)
                
            elif char == '#':
                res+=res
                    
            elif char == '*':
                if res:
                    res.pop()
                    
            else:
                res.reverse()
                
        return "".join(res)
