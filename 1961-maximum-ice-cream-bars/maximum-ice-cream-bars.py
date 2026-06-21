class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs)
        count = [0] * (n+1)
        for i in costs:
            count[i] = count[i] + 1

        for i in range (1,n+1):
            count[i] = count[i-1] + count[i]
        
        result = [0] * len(costs)
        for i in range(len(costs)-1,-1,-1):
            v = costs[i]
            result[count[v]-1] = v
            count[v] -=1
        
        maxice = 0
        for i in result:
            if coins < i:
                return maxice
            else:
                coins-= i 
                maxice+=1
        return maxice