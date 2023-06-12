from collections import deque

n, m = map(int, input().split())

board = []
wall_loc = []

for _ in range(n):
    board.append(list(map(int, list(input()))))

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def range_check(i, j):
    if 0 <= i < n and 0 <= j < m: return True
    else: return False

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            zero_count = 0
            for gap in gaps:
                next_i = i + gap[0]
                next_j = j + gap[1]
                if range_check(next_i, next_j):
                    if board[next_i][next_j] == 0: zero_count += 1
            if zero_count >= 2:
                wall_loc.append((i, j))

def bfs():
    q = deque()
    visited = [[False] * m for _ in range(n)]

    q.append((0, 0, 0))
    visited[0][0] = True
    
    while q:
        cur_i, cur_j, cur_step = q.popleft()
        if cur_i == n-1 and cur_j == m-1:
            return cur_step
        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]
            if range_check(next_i, next_j):
                if board[next_i][next_j] == 0 and not visited[next_i][next_j]:
                    q.append((next_i, next_j, cur_step+1))
                    visited[next_i][next_j] = True
    return -1

answer = 10**9
for i in range(len(wall_loc)):
    loc_i, loc_j = wall_loc[i]
    board[loc_i][loc_j] = 0
    result = bfs()
    if result != -1: answer = min(answer, result)
    board[loc_i][loc_j] = 1

if answer == 10**9: print(-1)
else: print(answer+1)