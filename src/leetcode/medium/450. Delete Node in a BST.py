class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        j = 0
        max_profit = 0
        while j < len(prices)-1:
            while j < len(prices)-1 and prices[i] >= prices[j+1]:
                i += 1
                j += 1
            while j < len(prices)-1 and prices[j] < prices[j+1]:
                j += 1
            max_profit += prices[j] - prices[i]
            i = j
            # j += 1
        return max_profit
    
prices = [7,1,5,3,6,4]

Solution().maxProfit(prices)