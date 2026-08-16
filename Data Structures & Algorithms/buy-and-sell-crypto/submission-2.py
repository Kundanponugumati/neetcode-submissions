class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1
        while(sell<len(prices)):
            if prices[sell] > prices[buy]:
                max_profit = max(prices[sell] - prices[buy],max_profit)
            elif prices[sell] < prices[buy]:
                buy = sell
            sell+=1
        return max_profit
            



        