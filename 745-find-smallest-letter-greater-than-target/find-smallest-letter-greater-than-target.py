class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
                
        # If low goes out of bounds, wrap around to the 1st character
        return letters[low % len(letters)]
