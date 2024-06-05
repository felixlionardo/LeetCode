class Solution(object):
    def maxProfit(self, prices):
        lowest_stock = prices[0]
        max_profit = 0
        for x in prices:
            lowest_stock = min(x, lowest_stock)
            max_profit = max(x-lowest_stock, max_profit)
        
        return max_profit
            
            
        