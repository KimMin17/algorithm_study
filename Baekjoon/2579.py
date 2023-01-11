n = int(input())

stair = []

for _ in range(n):
    stair.append(int(input()))

dp = [0] * n

if n >= 3:
    dp[0] = stair[0]
    dp[1] = dp[0] + stair[1]
    dp[2] = max(dp[0], stair[1]) + stair[2]

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

    print(dp[-1])
else:
    print(sum(stair))