class Solution:
    def isPalindrome(self, s):
        # code here
        n = len(s)
        left = 0
        right = n-1
        while(left<=right):
            if(s[left] != s[right]):
                return False
            left+=1
            right-=1
        return True