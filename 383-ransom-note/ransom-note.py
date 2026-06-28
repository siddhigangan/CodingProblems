class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = {}
        for i in ransomNote:
            if i in rn:
                rn[i] +=1
            else:
                rn[i] = 1
 
        mag = {}
        for j in magazine:
            if j in mag:
                mag[j] += 1
            else:
                mag[j] = 1

        for key,val in rn.items():
            if key not in mag or val > mag[key]:
                return False
        
        return True