class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1] == nums[i+2]:
                i += 3       # skip the triplet
            else:
                return nums[i]
        return nums[-1]      # single element is at the end