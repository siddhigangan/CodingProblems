class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        maxi = 0
        for i in gain:
            curr += i
            maxi = max(curr,maxi)
        return maxi
