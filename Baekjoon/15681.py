import sys
sys.setrecursionlimit(10**5)

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
dp = [-1] * (n+1)

for _ in range(n-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (n+1)
def dfs(node):
    if dp[node] != -1: return dp[node]
    visited[node] = True
    total = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            total += dfs(next_node)
    dp[node] = total
    return dp[node]

dfs(r)

query = []
for _ in range(q):
    query.append(int(input()))

for q in query:
    print(dp[q])