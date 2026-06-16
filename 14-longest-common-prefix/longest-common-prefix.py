class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Loop through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check this character against all other strings
            for string in strs[1:]:
                # If out of bounds or characters don't match, return the prefix found so far
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
                    
        return strs[0]
