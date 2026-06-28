class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be isomorphic
        if len(s) != len(t):
            return False
            
        map_s_to_t = {}
        map_t_to_s = {}
        
        # Iterate through both strings simultaneously using zip
        for char_s, char_t in zip(s, t):
            
            # Check mapping from s to t
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t
                
            # Check mapping from t to s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
                
        return True
