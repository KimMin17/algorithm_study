n, m = map(int, input().split())

men = list(map(int, input().split()))
women = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]

men.sort()
women.sort()

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(men[i-1] - women[j-1])
        elif i > j:
            dp[i][j] = min(dp[i-1][j-1] + abs(men[i-1] - women[j-1]), dp[i-1][j])
        else:
            dp[i][j] = min(dp[i-1][j-1] + abs(men[i-1] - women[j-1]), dp[i][j-1])

print(dp[n][m])