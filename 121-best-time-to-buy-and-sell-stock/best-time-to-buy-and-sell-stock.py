class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1  # Start 'sell' right next to 'buy'
        max_profit = 0

        # Move the sell pointer from left to right
        while sell < len(prices):
            # If it's a profitable transaction, calculate profit
            if prices[buy] < prices[sell]:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)
            else:
                # If prices[sell] is lower than prices[buy], 
                # we found a new lowest point! Move 'buy' here.
                buy = sell
                
            sell += 1  # Always move the sell pointer forward
            
        return max_profit
