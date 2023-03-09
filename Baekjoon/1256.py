n, m, k = map(int, input().split())

dp = [[1] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[n][m] < k:
    print(-1)
    exit()

i, j = n, m
answer = ""
for _ in range(n+m):
    check = dp[i-1][j]
    if i == 0:
        answer += 'z'
        j -= 1
    elif j == 0:
        answer += 'a'
        i -= 1
    elif check >= k:
        answer += 'a'
        i -= 1
    else:
        k -= check
        answer += 'z'
        j -= 1

print(answer)