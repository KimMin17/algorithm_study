from collections import deque

k = int(input())

def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        v1, v2 = map(int, input().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    q = deque()
    visited = [0] * (v+1)

    while True:
        for i in range(1, v+1):
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                break
            
        if len(q) == 0: break

        while q:
            cur = q.popleft()
            color = visited[cur]
            for adj in graph[cur]:
                if visited[adj] == color: return "NO"
                elif visited[adj] == 0:
                    q.append(adj)
                    visited[adj] = -color
    return "YES"

answers = []
for _ in range(k):
    answers.append(solve())

for answer in answers:
    print(answer)