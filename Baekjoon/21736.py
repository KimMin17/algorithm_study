from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

q = deque()

def find_cur_loc():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "I":
                return (i, j)

cur_i, cur_j = find_cur_loc()
visited = [[False] * m for _ in range(n)]

q.append((cur_i, cur_j))
visited[cur_i][cur_j] = True

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def range_check(i, j):
    if 0 <= i < n and 0 <= j < m: return True
    return False

answer = 0
while q:
    cur_i, cur_j = q.popleft()

    for gap in gaps:
        next_i, next_j = cur_i + gap[0], cur_j + gap[1]
        if range_check(next_i, next_j):
            if not visited[next_i][next_j] and graph[next_i][next_j] != 'X':
                if graph[next_i][next_j] == 'P': answer += 1
                q.append((next_i, next_j))
                visited[next_i][next_j] = True

if answer == 0: print("TT")
else: print(answer)