from collections import deque

n, m = tuple(map(int, input().split(" ")))

conn = [[] for _ in range(n+1)]

max_count = 0

for i in range(m):
    a, b = tuple(map(int, input().split(" ")))
    conn[b].append(a)

for i in range(1, n+1):
    q = deque()
    visited = [False for _ in range(n+1)]

    q.append(i)
    visited[i] = True
    count = 1
    
    while q:
        cur = q.popleft()
        for node in conn[cur]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                count += 1

    if count > max_count:
        results = [i]
        max_count = count
    elif count == max_count:
        results.append(i)

for result in results:
    print(result, end = " ")