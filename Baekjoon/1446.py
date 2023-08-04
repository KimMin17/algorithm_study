n, d = map(int, input().split())

INF = 10**9

dp = [INF] * 10001
conn = [[] for _ in range(10001)]

for _ in range(n):
    start, dest, dist = map(int, input().split())
    conn[dest].append((dist, start))

def dfs(node):
    if dp[node] != INF: return dp[node]

    dp[node] = node

    for i in range(node):
        to_node_dist = node-i
        for dist, start in conn[node]:
            if i == start: to_node_dist = min(to_node_dist, dist)
        dp[node] = min(dp[node], dfs(i)+to_node_dist)
    
    return dp[node]

print(dfs(d))