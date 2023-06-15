str1 = input()
str2 = input()

s1 = len(str1)
s2 = len(str2)

dp = [[0] * (s2+1) for _ in range(s1+1)]

answer = 0

def solve(n, m):
    result = 0
    for i in range(n):
        for j in range(m):
            result = max(result, dp[i][j])
    return result

for i in range(1, s1+1):
    for j in range(1, s2+1):
        if str1[i-1] == str2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        answer = max(answer, dp[i][j])

print(answer)