import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

N = 0
Y = 1

graph = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

def solve(node):
    visited[node] = True
    dp[node][N] = 0
    dp[node][Y] = 1
    for c in graph[node]:
        if visited[c]: continue
        solve(c)
        dp[node][N] += dp[c][Y]
        dp[node][Y] += min(dp[c][N], dp[c][Y])

solve(1)

print(min(dp[1][Y], dp[1][N]))