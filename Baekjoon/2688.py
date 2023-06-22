t = int(input())

dp = [[0] * 10 for _ in range(66)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def solve(n):
    for i in range(10):
        for j in range(i+1):
            dp[n][i] += dp[n-1][j]
inputs = []
for _ in range(t):
    inputs.append(int(input()))

for i in range(max(inputs)+1):
    solve(i)

for i in inputs:
    print(sum(dp[i]))