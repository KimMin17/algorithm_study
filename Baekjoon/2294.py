n, k = map(int, input().split())

coins = []

for _ in range(n):
    coin = int(input())
    if coin not in coins:
        coins.append(coin)

dp = [0] * (max(*coins, k) + 1)

for coin in coins:
    dp[coin] = 1

INF = 10 ** 9

for i in range(1, k+1):
    answer = INF
    choice = []
    for coin in coins:
        if i - coin >= 0:
            if dp[i-coin] != 0:
                choice.append(i-coin)

    for c in choice:
        if answer != 0 and dp[c] < answer: answer = dp[c]
    
    if answer != INF:
        if dp[i] == 0: dp[i] = answer+1
        else: dp[i] = min(dp[i], answer+1)

if dp[k] == 0: print(-1)
else: print(dp[k])