from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()  # [1, 3, 3, 3]
        
        n = len(cost) % 3
        total = 0
        
        # 1. Add the leftovers from the BEGINNING of the sorted list
        if n != 0:
            total += sum(cost[:n])  # Grabs the cheapest leftover items
            
        # 2. Process the remaining perfect triplets from index n to the end
        # We use a secondary counter (j) starting at 0 to track triplet indices
        j = 0
        for i in range(n, len(cost)):
            if j % 3 != 0:
                total += cost[i]
            j += 1
            
        return total
