import sys
from collections import deque

input = sys.stdin.readline

h, w = tuple(map(int, input().split()))

board = []

for _ in range(h):
    board.append(list(input()))

def find_coin(h, w):
    loc = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'o':
                loc.append([i, j])
    
    return tuple(loc)

coin1_loc, coin2_loc = find_coin(h, w)

q = deque()

q.append((coin1_loc, coin2_loc, 0))
visited = [(coin1_loc, coin2_loc)]

def move_coin(cur_loc, gap):
    next_i = cur_loc[0] + gap[0]
    next_j = cur_loc[1] + gap[1]

    if h <= next_i or next_i < 0 or w <= next_j or next_j < 0:
        return [-1, -1]
    elif board[next_i][next_j] == '#': return cur_loc
    else: return [next_i, next_j]

while(q):
    cur_coin1, cur_coin2, cur_step = q.popleft()

    if cur_step >= 10:
        print(-1)
        exit()

    gaps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    for gap in gaps:
        next_coin1 = move_coin(cur_coin1, gap)
        next_coin2 = move_coin(cur_coin2, gap)

        if next_coin1 == [-1, -1] and next_coin2 != [-1, -1]:
            print(cur_step + 1)
            exit()
        elif next_coin1 != [-1, -1] and next_coin2 == [-1, -1]:
            print(cur_step + 1)
            exit()
        elif next_coin1 == next_coin2: continue
        elif (next_coin1, next_coin2) not in visited:
            q.append((next_coin1, next_coin2, cur_step + 1))
            visited.append((next_coin1, next_coin2))

print(-1)