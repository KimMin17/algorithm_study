from collections import deque

n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(input()))

r_loc = []
b_loc = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            r_loc = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            b_loc = [i, j]
            board[i][j] = '.'

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def move(i, j, gap):
    while True:
        next_i, next_j = i + gap[0], j + gap[1]
        if board[next_i][next_j] == 'O': return (-1, -1)
        elif board[next_i][next_j] != '.': return (i, j)        
        i, j = next_i, next_j

def bfs():
    q = deque()
    visited = []
    
    gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    q.append((r_loc[0], r_loc[1], b_loc[0], b_loc[1], 0))
    visited.append((r_loc[0], r_loc[1], b_loc[0], b_loc[1]))

    while q:
        ri, rj, bi, bj, count = q.popleft()
        if count > 10: break

        for gap in gaps:
            cur_ri, cur_rj, cur_bi, cur_bj = ri, rj, bi, bj
            r_in_hole = False
            b_in_hole = False
            for _ in range(2):
                if not r_in_hole: board[cur_ri][cur_rj] = 'R'
                if not b_in_hole: board[cur_bi][cur_bj] = 'B'
                if not r_in_hole: next_ri, next_rj = move(cur_ri, cur_rj, gap)
                if not b_in_hole: next_bi, next_bj = move(cur_bi, cur_bj, gap)
                if not r_in_hole: board[cur_ri][cur_rj] = '.'
                if not b_in_hole: board[cur_bi][cur_bj] = '.'

                if not r_in_hole: cur_ri, cur_rj = next_ri, next_rj
                if not b_in_hole: cur_bi, cur_bj = next_bi, next_bj

                if next_ri == -1 and next_rj == -1:
                    r_in_hole = True
                if next_bi == -1 and next_bj == -1:
                    b_in_hole = True
                    break
            
            if b_in_hole: continue
            elif r_in_hole:
                print(count+1)
                exit()

            if (cur_ri, cur_rj, cur_bi, cur_bj) not in visited:
                visited.append((cur_ri, cur_rj, cur_bi, cur_bj))
                q.append((cur_ri, cur_rj, cur_bi, cur_bj, count+1))
    print(-1)

bfs()