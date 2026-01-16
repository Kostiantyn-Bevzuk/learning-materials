class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        current_sum = 0
        curr_counter = 0
        counter = [float("inf")]

        def dp(current_sum, curr_counter):
            if current_sum > amount:
                return
            elif current_sum == amount:
                counter[0] = min(counter[0], curr_counter)

            for i in range(len(coins)):
                curr_counter += 1
                current_sum += coins[i]
                dp(current_sum, curr_counter)
                curr_counter -= 1
                current_sum -= coins[i]

        dp(curr_counter, current_sum)
        return -1 if counter[0] == float("inf") else counter[0]

# Top down (memoization)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cache = {0: 0}

        def dp(curr_amount):
            if curr_amount in cache:
                return cache[curr_amount]
            if curr_amount < 0:
                return float("inf")

            curr_min = float("inf")
            for coin in coins:
                diff = curr_amount - coin
                if diff >= 0:
                    curr_min = min(curr_min, 1 + dp(diff))

            cache[curr_amount] = curr_min
            return cache[curr_amount]

        result = dp(amount)

        return result if result < float("inf") else -1

# Bottom up

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        dp = [0 for _ in range(amount+1)]

        for i in range(1, len(dp)):
            curr_min = float("inf")
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                curr_min = min(curr_min, 1 + dp[diff])
            dp[i] = curr_min

        return dp[-1] if dp[-1] < float("inf") else -1





# coins = [5, 2, 1]
# amount = 7
# [0, 0, 0, 0, 0, 0, 0, 0]
# 
# Solution().coinChange(coins, amount)