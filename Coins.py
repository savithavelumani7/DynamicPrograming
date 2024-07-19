
def smallval(coins, amount):
    dp = [amount + 1] * (amount + 1)
    print(dp)
    dp[0] = 0
    print(dp)
    for coin in coins:    #coin = 1
        for i in range(coin, amount + 1):   # i = 1 to 12    1st(i=1)
            dp[i] = min(dp[i], dp[i - coin] + 1)    #min(12,1)=1
            print (dp)

    return dp[amount] if dp[amount] != amount + 1 else -1


coins=list(map(int,input().split()))
amount=int(input())
result=smallval(coins,amount)
print(result)