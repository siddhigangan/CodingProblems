class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        freq = [0] * 101  # index 0..100 maps to values -50..50

        def find_xth_smallest(x):
            count = 0
            for i in range(50):           # only check negatives: index 0..49 → values -50..-1
                count += freq[i]
                if count >= x:
                    return i - 50         # convert index back to value
            return 0                      # x-th smallest is not negative

        # Build initial window
        for i in range(k):
            freq[nums[i] + 50] += 1

        res.append(find_xth_smallest(x))

        # Slide the window
        for right in range(k, n):
            freq[nums[right] + 50] += 1          # add incoming element
            freq[nums[right - k] + 50] -= 1      # remove outgoing element
            res.append(find_xth_smallest(x))

        return res