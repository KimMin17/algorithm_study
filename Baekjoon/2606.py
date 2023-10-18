from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (n+1)
answer = 0

def bfs(start):
    global answer
    q = deque()
    q.append(start)

    visited[start] = True

    while q:
        cur = q.popleft()
        answer += 1
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)

bfs(1)

print(answer-1)