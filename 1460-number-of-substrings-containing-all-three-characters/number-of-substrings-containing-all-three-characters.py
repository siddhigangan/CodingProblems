class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Tracks the last seen index of 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            last_seen[char] = i
            # If all three characters have been seen at least once
            if min(last_seen.values()) >= 0:
                # Any substring starting from index 0 up to the minimum index is valid
                count += min(last_seen.values()) + 1
                
        return count
