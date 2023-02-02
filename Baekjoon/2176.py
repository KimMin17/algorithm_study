'''
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
    graph[i][i] = 0

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

'''

import sys
import heapq

limit_number = 200000
sys.setrecursionlimit(limit_number)

n, m = map(int, sys.stdin.readline().rstrip().split())

nodes = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
    
INF = sys.maxsize

def Dijsktra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost+next_cost, next_node])
    return distances

dist = Dijsktra(2)

start, dest = 1, 2

start_cost = dist[start]

dp = [-1] * (n+1)

def dfs(start):
    if dp[start] != -1: return dp[start]
    
    result = 0
    for node, node_dist in nodes[start]:
        if dist[node] < start_cost:
            result += dfs(node)
    dp[start] = result
    return result

dp[dest] = 1
print(dfs(start))