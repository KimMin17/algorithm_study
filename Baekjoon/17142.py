from itertools import combinations
from collections import deque

n, m = map(int, input().split())

graph= []

INF = 10**5

for _ in range(n):
    graph.append(input().split())

non_active_v = []

left_count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] != '1': left_count += 1
        if graph[i][j] == '2':
            non_active_v.append((i, j))

combs = combinations(range(len(non_active_v)), m)

answer = INF

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def range_check(i, j):
    if 0 <= i < n and 0 <= j < n: return True
    return False

def clear_graph():
    for i in range(n):
        for j in range(n):
            if graph[i][j] != '1': graph[i][j] = '0'
    for vi, vj in non_active_v: graph[vi][vj] = '2'


def bfs(comb):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    for c in comb:
        vi = non_active_v[c][0]
        vj = non_active_v[c][1]

        q.append((vi, vj, 0))
        visited[vi][vj] = True
        graph[vi][vj] = '*'

    count = m
    while q:
        cur_i, cur_j, cur_t = q.popleft()
        for gap in gaps:
            next_i, next_j = cur_i + gap[0], cur_j + gap[1]
            if range_check(next_i, next_j):
                if graph[i][j] != '1' and not visited[i][j]:
                    count += 1
                    graph[next_i][next_j] = '*'
                    if graph[next_i][next_j] == '2': q.append((next_i, next_j, cur_t))
                    else: q.append((next_i, next_j, cur_t+1))
                    visited[next_i][next_j] = True
                    
                    if count == left_count: return cur_t + 1
    
    return INF

for comb in combs:
    answer = min(answer, bfs(comb))
    clear_graph()

if answer == INF: print(-1)
else: print(answer)