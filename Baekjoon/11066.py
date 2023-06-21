import sys

input = sys.stdin.readline

dp = None
sums = None

INF = 10**9

def get_slice_sum(start, end):
    global sums
    if start == 0: return sums[end]
    else: return sums[end] - sums[start-1]

def dfs(start, end, l):
    if dp[start][end] != INF:
        return dp[start][end]

    if end - start == 1:
        dp[start][end] = l[start] + l[end]
        return dp[start][end]
    
    for i in range(start, end):
        dp[start][end] = min(dp[start][end], dfs(start, i, l) + dfs(i+1, end, l))
    dp[start][end] += get_slice_sum(start, end)
    return dp[start][end]

def solve(n, l):
    global dp
    global sums
    dp = [[INF] * n for _ in range(n)]
    sums = [0] * n
    for i in range(n): dp[i][i] = 0
    sums[0] = l[0]
    for i in range(1, n): sums[i] = sums[i-1] + l[i]
    dfs(0, n-1, l)
    return dp[0][n-1]

testcase = int(input())

answers = []
for _ in range(testcase):
    n = int(input())
    l = list(map(int, input().split()))
    
    answers.append(solve(n, l))

for answer in answers:
    print(answer)