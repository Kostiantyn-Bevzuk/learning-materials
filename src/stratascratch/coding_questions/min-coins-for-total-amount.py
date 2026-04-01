def min_coins(input_):
    """
    :type input: Dict[str, Union[int, List[int]]]
    :rtype: int
    """

    amount = input_["amount"]
    coins = sorted(input_["coins"])
    
    dp = [0 for _ in range(amount+1)]
    
    for index in range(1, len(dp)):
        min_current = float("inf")
        for coin in coins:
            diff = index - coin
            if diff < 0:
                break
            min_current = min(min_current, 1 + dp[diff])
        dp[index] = min_current
    
    return -1 if dp[-1] == float("inf") else dp[-1]

input_ = {"coins": [1, 2, 5], "amount": 11}

min_coins(input_)