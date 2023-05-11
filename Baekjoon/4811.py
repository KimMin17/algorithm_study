MAX_N = 32

dp = [[0] * MAX_N for _ in range(MAX_N)]

def dfs(f_n, h_n):
    if dp[f_n][h_n] != 0: return dp[f_n][h_n]
    if f_n == 0: return 1

    result = dfs(f_n-1, h_n+1)
    if h_n != 0: result += dfs(f_n, h_n-1)
    dp[f_n][h_n] = result
    return result

def solve(n):
    return dfs(n, 0)

answers = []
while True:
    n = int(input())
    if n == 0: break
    answers.append(solve(n))

for answer in answers:
    print(answer)