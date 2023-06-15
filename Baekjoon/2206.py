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

def bfs():
    q = deque()
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]

    q.append((0, 0, 1, 0))
    visited[0][0][0] = True

    while q:
        cur_i, cur_j, cur_step, break_used = q.popleft()
        if cur_i == n-1 and cur_j == m-1: return cur_step

        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]
            if range_check(next_i, next_j):
                if board[next_i][next_j] == 0 and not visited[next_i][next_j][break_used]:
                    q.append((next_i, next_j, cur_step+1, break_used))
                    visited[next_i][next_j][break_used] = True
                elif board[next_i][next_j] == 1 and break_used == 0 and not visited[next_i][next_j][1]:
                    q.append((next_i, next_j, cur_step+1, 1))
                    visited[next_i][next_j][1] = True
    
    return -1

print(bfs())