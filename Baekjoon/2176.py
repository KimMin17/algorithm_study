from queue import PriorityQueue

n, m = map(int, input().split())
n += 1

INF = 20000
dist = [INF] * n
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    v1, v2, d = map(int, input().split())
    graph[v1][v2] = d
    graph[v2][v1] = d

for i in range(n):
    graph[n][n] = 0

start, dest = 1, 2

def dijkstra(start):
    dist = [INF] * n
    visited = [False] * n
    visited[0] = True

    for i in range(n):
        dist[i] = graph[start][i]
    
    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        next_dist, next_node = q.get()
        visited[next_node] = True
        for i in range(1, n):
            cost = next_dist + graph[next_node][i]
            dist[i] = min(dist[i], cost)

            if not visited[i]:
                q.put((dist[i], i))
                visited[i] = True

    return dist

dist = dijkstra(dest)
start_cost = dist[start]

dp = [[-1] * n for _ in range(n)]

def dfs(start, dest):
    if dp[start][dest] != -1: return dp[start][dest]
    if start == dest: return 1
    
    result = 0
    for i in range(n):
        if graph[start][i] != INF:
            result += dfs(i, dest)
    dp[start][dest] = result
    return result

print(dfs(start, dest))