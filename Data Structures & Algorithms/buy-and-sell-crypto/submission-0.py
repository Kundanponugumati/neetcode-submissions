class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            local_max_profit = 0
            for j in range(i+1,len(prices),1):
                local_max_profit = max(prices[j]-prices[i],local_max_profit)
            max_profit = max(max_profit,local_max_profit)
        return max_profit

        