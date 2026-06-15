from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = 0
        right = n-1

        total =leftmax=rightmax=0
        while(left<=right):
            if(height[left]<=height[right]):
                if(leftmax>height[left]):
                    total+=leftmax - height[left]
                else:
                    leftmax = height[left]
                left+=1
            else:
                if(rightmax>height[right]):
                    total+=rightmax - height[right]
                else:
                    rightmax = height[right]
                right-=1
        return total