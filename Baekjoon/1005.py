t = int(input())
answers = []

def dfs(w, dp, graph, times):
    if dp[w] != -1: return dp[w]

    max_pre_time = 0
    for pre in graph[w]:
        max_pre_time = max(max_pre_time, dfs(pre, dp, graph, times))
    dp[w] = max_pre_time + times[w]
    return dp[w]

def solve():
    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]
    times = list(map(int, input().split()))

    dp = [-1] * n

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y-1].append(x-1)
    
    return dfs(int(input())-1, dp, graph, times)

for _ in range(t):
    answers.append(solve())

for answer in answers:
    print(answer)