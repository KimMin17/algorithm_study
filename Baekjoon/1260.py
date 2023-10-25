from collections import deque
import sys

sys.setrecursionlimit = 10000

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(n+1):
    graph[i].sort()


def bfs(start):
    q = deque()
    visited = [False] * (n+1)

    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)        

visited_dfs = [False] * (n+1)
visited_dfs[v] = True
def dfs(start):
    print(start, end=" ")
    for adj in graph[start]:
        if not visited_dfs[adj]:
            visited_dfs[adj] = True
            dfs(adj)

dfs(v)
print()
bfs(v)