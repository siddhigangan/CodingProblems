from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mag = Counter(magazine)

        for key, val in rn.items():
            if mag[key] < val: # Counter returns 0 automatically if key is missing
                return False
        return True
