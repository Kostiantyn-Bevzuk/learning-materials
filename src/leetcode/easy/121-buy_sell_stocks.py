class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_value = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif (
                (prices[l] < prices[r] and r == len(prices) - 1)
                or (prices[l] < prices[r] and prices[r] > prices[r+1])
            ):
                max_value += prices[r] - prices[l]
                l = r+1
                r = l+1
            else:
                r += 1
        return max_value

prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]

print(Solution().maxProfit(prices=prices))