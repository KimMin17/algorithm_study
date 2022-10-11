num, target = tuple(map(int, input().split(" ")))

MAX = 100000000

dp = [MAX for i in range(target + 1)]
dp[num] = 0

for i in range(num + 1, target + 1):
    if i % 2 != 0:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)

print(dp[target])