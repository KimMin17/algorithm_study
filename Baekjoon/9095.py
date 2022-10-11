n = int(input())
arr = []
results = []

for i in range(n):
    arr.append(int(input()))

m = max(arr)
dp = [0 for i in range(m + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, m + 1):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for item in arr:
    results.append(dp[item])

for result in results:
    print(result)