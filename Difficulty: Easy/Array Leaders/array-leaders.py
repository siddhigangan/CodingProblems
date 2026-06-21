class Solution:
    def leaders(self, arr):
        n = len(arr)
        res = []
        
        # The rightmost element is always a leader
        max_from_right = arr[n-1]
        res.append(max_from_right)
        
        # Traverse the array from right to left
        for i in range(n-2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                res.append(max_from_right)
                
        # Reverse the result array to restore original order
        return res[::-1]
