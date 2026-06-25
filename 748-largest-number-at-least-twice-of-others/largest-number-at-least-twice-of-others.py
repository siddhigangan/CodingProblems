class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_no = max(nums)
        for i in nums:
            if(i != max_no and i!=0 and (max_no / i)>=2):
                continue
            elif (i == max_no or i == 0):
                continue
            else:
                return -1
        return nums.index(max_no)