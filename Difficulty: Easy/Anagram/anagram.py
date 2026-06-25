class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        s1l = list(s1)
        s2l = list(s2)
        s1l.sort()
        s2l.sort()
        if(len(s1l) != len(s2l)):
            return False
        for i in range(len(s1l)):
            if s1l[i] != s2l[i]:
                return False
        return True