import sys
from collections import deque

input = sys.stdin.readline

r, c, t = map(int, input().split())

board = []

for _ in range(r):
    board.append(list(map(int, input().split())))

u_route = []
d_route = []

def range_check(i, j):
    if 0 <= i < r and 0 <= j < c:
        if board[i][j] != -1: return True
    return False

u_loc = [0, 0]
d_loc = [0, 0]
def find_air_cleaner():
    for i in range(r):
        if board[i][0] == -1:
            u_loc[0], d_loc[0] = i, i+1
            return

def find_u_route():
    u_route.append(u_loc)
    
    for i in reversed(range(u_loc[0])):
        u_route.append([i, 0])
    for j in range(1, c):
        u_route.append([0, j])
    for i in range(1, u_loc[0]+1):
        u_route.append([i, c-1])
    for j in reversed(range(1, c-1)):
        u_route.append([u_loc[0], j])

def find_d_route():
    d_route.append(d_loc)
    
    for i in range(d_loc[0]+1, r):
        d_route.append([i, 0])
    for j in range(1, c):
        d_route.append([r-1, j])
    for i in reversed(range(d_loc[0], r-1)):
        d_route.append([i, c-1])
    for j in reversed(range(1, c-1)):
        d_route.append([d_loc[0], j])

gaps = [[0, 1], [-1, 0], [0, -1], [1, 0]]
changes = deque()
def do_diffusion(i, j):
    total_loss = 0
    loss = board[i][j] // 5
    for gap in gaps:
        next_i = i + gap[0]
        next_j = j + gap[1]
        if range_check(next_i, next_j):  
            changes.append((next_i, next_j, loss))
            total_loss -= loss
    changes.append((i, j, total_loss))

def diffusion():
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                do_diffusion(i, j)

def clean_air(route):
    for k in range(len(route)-1):
        i, j = tuple(route[k])
        next_i, next_j = tuple(route[k+1])

        board[i][j] = board[next_i][next_j]
    
    board[route[0][0]][route[0][1]] = -1
    board[route[0][0]][route[0][1]+1] = 0

def change_board():
    while changes:
        i, j, diff = changes.popleft()
        board[i][j] +=  diff

find_air_cleaner()
find_u_route()
find_d_route()

for _ in range(t):
    diffusion()
    change_board()
    clean_air(u_route)
    clean_air(d_route)

answer = 0

for i in range(r):
    for j in range(c):
        answer += board[i][j]

print(answer+2)