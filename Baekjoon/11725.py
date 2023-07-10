from collections import deque

n = int(input())

conn = [[] for i in range(n+1)]

for _ in range(n-1):
    n1, n2 = map(int, input().split())
    conn[n1].append(n2)
    conn[n2].append(n1)

parents = [0] * (n+1)

q = deque()
q.append(1)
parents[1] = 1

while q:
    cur = q.popleft()
    for child in conn[cur]:
        if parents[child] == 0:
            q.append(child)
            parents[child] = cur

for i in range(2, n+1):
    print(parents[i])