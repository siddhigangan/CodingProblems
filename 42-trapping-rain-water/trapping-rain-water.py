from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
            
        # Initialize lists with zeros to avoid IndexError
        prefixmax = [0] * n
        suffixmax = [0] * n
        
        # Fill prefix maximums
        prefixmax[0] = height[0]
        for i in range(1, n):
            prefixmax[i] = max(prefixmax[i-1], height[i])
            
        # Fill suffix maximums
        suffixmax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffixmax[i] = max(suffixmax[i+1], height[i])

        total = 0
        for i in range(n):
            leftmax = prefixmax[i]
            rightmax = suffixmax[i]

            # Simplified logic: every bar traps water up to the min boundary
            total += min(leftmax, rightmax) - height[i]
            
        return total
