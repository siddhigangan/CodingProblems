class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for char in s:
            if char.isalnum():
                st = st + char
        
        st = st.lower()
        stt = st[::-1]
        return st == stt