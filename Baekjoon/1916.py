from queue import PriorityQueue

n = int(input())
m = int(input())
n += 1

INF = 10000000000000
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    v1, v2, c = map(int, input().split())
    graph[v1][v2] = c
    graph[v2][v1] = c

for i in range(n):
    graph[i][i] = 0

start, dest = map(int, input().split())

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

dist = dijkstra(start)
print(dist[dest])