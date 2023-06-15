dp = None

def dfs(start, end, l):
    if dp[start][end] != 10**9: return dp[start][end]

    if end - start == 1:
        dp[start][end] = l[start] + l[end]
        return dp[start][end]
    
    for i in range(start, end):
        dp[start][end] = min(dp[start][end], dfs(start, i, l) + dfs(i+1, end, l))
    return dp[start][end]

def trace(start, end):
    if end - start == 2:
        return dp[start][end]
    result = 0
    for i in range(start, end):
        if dp[start][i] + dp[i+1][end] == dp[start][end]:
            result += trace(start, i)
            result += trace(i+1, end)
            break
    result += dp[start][end]
    return result

def solve(n, l):
    global dp
    dp = [[10**9] * n for _ in range(n)]
    for i in range(n): dp[i][i] = l[i]

    dfs(0, n-1, l)
    print(dp[0][n-1])
    return trace(0, n-1)

testcase = int(input())

answers = []
for _ in range(testcase):
    n = int(input())
    l = list(map(int, input().split()))
    
    answers.append(solve(n, l))

for answer in answers:
    print(answer)