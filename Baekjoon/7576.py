import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ripe_tomas = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ripe_tomas.append((i, j, 0))

max_step = 0
while ripe_tomas:
    cur_x, cur_y, cur_step = ripe_tomas.popleft()
    max_step = max(max_step, cur_step)
    for i in range(4):
        new_x = cur_x + dx[i]
        new_y = cur_y + dy[i]

        if 0 > new_x or new_x >= n or 0 > new_y or new_y >= m: continue

        if arr[new_x][new_y] == 0:
            arr[new_x][new_y] = 1
            ripe_tomas.append((new_x, new_y, cur_step + 1))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            max_step = -1

print(max_step)