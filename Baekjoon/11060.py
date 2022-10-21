n = int(input())
max = 1000000
maze = list(map(int, input().split(" ")))
dp = [max for _ in range(n)]

dp[0] = 0

for i in range(n):
    for j in range(maze[i]+1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
            
if dp[n-1] == max: print("-1")
else: print(dp[n-1])