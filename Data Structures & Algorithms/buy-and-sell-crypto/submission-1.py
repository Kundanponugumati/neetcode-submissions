class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            local_profit = 0
            for j in range(i+1,len(prices),1):
                if prices[j] - prices[i] >0:
                    local_profit = max(local_profit,prices[j] - prices[i])
            max_profit = max(max_profit,local_profit)
        return max_profit
                



        