n = int(input())

arr = []

INF = 1 << 32

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n  for _ in range(n)]

for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = INF
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0]*arr[k][1]*arr[j][1])
print(dp[0][n-1])