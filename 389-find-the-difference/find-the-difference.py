class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)
        tc = Counter(t)
        
        for key,val in tc.items():
            if key not in sc or val > sc[key]:
                return key
        return -1