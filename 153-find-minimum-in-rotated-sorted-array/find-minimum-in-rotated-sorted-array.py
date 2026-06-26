class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        # Loop stops when low and high meet at the minimum element
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than high element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid)
            else:
                high = mid
                
        return nums[low]
