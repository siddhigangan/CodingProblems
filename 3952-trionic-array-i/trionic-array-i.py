from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:  # A valid Trionic array requires at least 4 elements
            return False
            
        i = 0
        
        # ---------------------------------------------------------
        # BLOCK 1: Move through the STRICTLY INCREASING section
        # ---------------------------------------------------------
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            
        # Validation 1: If i didn't move, there was no initial increase.
        if i == 0: 
            return False
            
        # ---------------------------------------------------------
        # BLOCK 2: Move through the STRICTLY DECREASING section
        # ---------------------------------------------------------
        start_dec = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
            
        # Validation 2: If i didn't move, there was no decreasing section.
        # If i reached the end, there is no room left for the final increase.
        if i == start_dec or i == n - 1:
            return False
            
        # BLOCK 3: Move through the FINAL STRICTLY INCREASING section
       
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            
        # Final Verification: If we successfully processed the entire array 
        return i == n - 1
