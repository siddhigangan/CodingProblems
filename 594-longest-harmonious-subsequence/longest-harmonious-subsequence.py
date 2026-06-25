import collections

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Count the frequency of each number
        counts = collections.Counter(nums)
        max_length = 0
        
        # Check if num + 1 exists to form a harmonious subsequence
        for num in counts:
            if num + 1 in counts:
                max_length = max(max_length, counts[num] + counts[num + 1])
                
        return max_length
