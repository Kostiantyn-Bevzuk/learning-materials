# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:

#         cache = {}

#         def backtrack(remain_amount, curr_index):
#             if (remain_amount, curr_index) in cache:
#                 return cache[(remain_amount, curr_index)]

#             if remain_amount == 0:
#                 return 1

#             if curr_index >= len(coins):
#                 return 0

#             diff = remain_amount - coins[curr_index]
#             if diff < 0:
#                 cache[(remain_amount, curr_index)] = backtrack(
#                     remain_amount, curr_index + 1
#                 )
#             else:
#                 cache[(remain_amount, curr_index)] = backtrack(
#                     diff, curr_index
#                 ) + backtrack(remain_amount, curr_index + 1)
#             return cache[(remain_amount, curr_index)]

#         return backtrack(amount, 0)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for row in range(len(coins)+1):
            dp[row][0] = 1

        # dp[i][j] how many coins at index i and on wards need to make j amount of money
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount+1): 
                diff = j - coins[i]
                if diff < 0:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i][diff] + dp[i+1][j]
        
        return dp[0][amount]
        

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        # for i in range(len(coins) - 1, -1, -1):
        #     for j in range(1, amount+1): 
        #         diff = j - coins[i]
        #         if diff < 0:
        #             dp[j] = dp[j]
        #         else:
        #             dp[j] = dp[diff] + dp[j]

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount+1): 
                diff = j - coins[i]
                if diff >= 0:
                    dp[j] = dp[diff] + dp[j]

        
        return dp[amount]
