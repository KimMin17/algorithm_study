from queue import PriorityQueue

n = int(input())
m = int(input())
n += 1

INF = 10000000000000
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    v1, v2, c = map(int, input().split())
    graph[v1][v2] = min(graph[v1][v2], c)

for i in range(n):
    graph[i][i] = 0

start, dest = map(int, input().split())

def dijkstra(start):
    dist = [INF] * n
    dist[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        cur_cost, cur_node = pq.get()

        if dist[cur_node] < cur_cost: continue

        for next_node in range(n):
            next_cost = graph[cur_node][next_node]
            if dist[next_node] > cur_cost + next_cost:
                dist[next_node] = cur_cost + next_cost
                pq.put((cur_cost + next_cost, next_node))

    return dist

dist = dijkstra(start)
print(dist[dest])