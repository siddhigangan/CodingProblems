class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Slice from index 1 to the end and sort it
        remaining = sorted(nums[1:])
        
        # Add the first element to the two smallest elements
        return nums[0] + remaining[0] + remaining[1]
