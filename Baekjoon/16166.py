from collections import deque

n = int(input())

lines = []

for _ in range(n):
    line = list(map(int, input().split()))
    del line[0]
    lines.append(set(line))

graph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if lines[i].intersection(lines[j]):
            graph[i][j] = 1
            graph[j][i] = 1

dest = int(input())
dest_line = []
start_lines = []

for i in range(n):
    if 0 in lines[i]:
        start_lines.append(i)
    if dest in lines[i]:
        dest_line.append(i)

q = deque()
visited = [False] * n

for start_line in start_lines:
    q.append((start_line, 0))
    visited[start_line] = True

while q:
    cur, step = q.popleft()
    if cur in dest_line:
        print(step)
        exit()
    for i in range(n):
        if graph[cur][i] == 1 and not visited[i]:
            q.append((i, step + 1))
            visited[i] = True
print(-1)