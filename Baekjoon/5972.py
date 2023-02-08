import heapq

n, m = map(int, input().split())

INF = 100000000

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    
    exist = False
    for conn in graph[s]:
        if conn[0] == e:
            exist = True
            if c < conn[1]:
                conn[1] = c
                break
    if not exist:
        graph[s].append([e, c])

    exist = False
    for conn in graph[e]:
        if conn[0] == s:
            exist = True
            if c < conn[1]:
                conn[1] = c
                break
    if not exist:
        graph[e].append([s, c])
            

def dijkstra(s, e):
    pq = []
    dist = [INF] * (n+1)

    heapq.heappush(pq, (0, s))

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > dist[cur_node]: continue
        for next_node, next_dist in graph[cur_node]:
            new_cost = cur_dist + next_dist
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return dist[e]

print(dijkstra(1, n))