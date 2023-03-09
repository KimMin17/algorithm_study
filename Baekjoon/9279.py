answers = []
INF = 10**9

def dfs(node, before, graph, dp):
    leaf_w = 5000
    w_sum = 0
    for i in range(1, n+1):
        if i != before and graph[node][i] != INF:
            w_sum += min(graph[node][i], dfs(i, node, graph, dp))

    if w_sum == 0: dp[node] = leaf_w
    else: dp[node] = w_sum

    return dp[node]

def solve(n, c):
    graph = [[INF] * (n+1) for _ in range(n+1)]
    dp = [INF] * (n+1)

    for _ in range(n-1):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
    
    answers.append(dfs(c, -1, graph, dp))

while True:
    try:
        n, c = map(int, input().split())
        solve(n, c)
    except :
        break

for answer in answers:
    print(answer)