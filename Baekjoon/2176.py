from heapq import heappop, heappush

n, m = map(int, input().split())

INF = 20000
dist = [INF] * n
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    v1, v2, d = map(int, input().split())
    graph[v1][v2] = d
    graph[v2][v1] = d

start = 1
end = 2

def dijkstra(start):
    visit = [False] * n
    priority_q = []
    for i in range(n):
        dist[i] = graph[start][i]



dijkstra()

