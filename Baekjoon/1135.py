n = int(input())
info = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(1, len(info)):
    graph[info[i]].append(i)

dp = [-1] * n

def dfs(node):
    if dp[node] != -1: return dp[node]
    if len(graph[node]) == 0:
        dp[node] = 1
        return dp[node]
    
    time_list = []

    for c in graph[node]:
        time_list.append(dfs(c))
    
    time_list.sort(reverse=True)
    for i in range(len(time_list)):
        time_list[i] += i
    dp[node] = max(time_list) + 1
    return dp[node]

print(dfs(0)-1)