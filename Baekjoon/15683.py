'''
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
'''

import sys

from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

board = []

for _ in range(r):
    board.append(list(map(int, input().split())))

cam_list = []
board_size = 0

for i in range(r):
    for j in range(c):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cam_list.append((i, j, board[i][j]))
        elif board[i][j] == 0: board_size += 1

U = 0
R = 1
D = 2
L = 3

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def get_direction(cam, rot):
    if cam == 1:
        return [rot]
    elif cam == 2:
        return [rot, (rot+2)%4]
    elif cam == 3:
        return [rot, (rot+1)%4]
    elif cam == 4:
        return [rot, (rot+1)%4, (rot+3)%4]
    elif cam == 5:
        return [U, R, D, L]

def range_check(i, j):
    if 0 <= i < r and 0 <= j < c:
        if board[i][j] == 6: return False
        return True
    return False

def fill_line(i, j, d, change_list):
    global board_size

    next_i = i + gaps[d][0]
    next_j = j + gaps[d][1]
    while range_check(next_i, next_j):
        if board[next_i][next_j] == 0:
            board[next_i][next_j] = 7
            board_size -= 1
            change_list.append((next_i, next_j))
        next_i = next_i + gaps[d][0]
        next_j = next_j + gaps[d][1]

def undo_line(change_list):
    global board_size

    while change_list:
        i, j = change_list.popleft()
        board[i][j] = 0
        board_size += 1

def use_cam(idx):
    global board_size
    global answer

    i, j, cam = cam_list[idx]

    for rot in range(4):
        change_list = deque()
        directions = get_direction(cam, rot)
        for d in directions:
            fill_line(i, j, d, change_list)
        if idx < len(cam_list) - 1: use_cam(idx+1)
        else: answer = min(answer, board_size)
        undo_line(change_list)

answer = 10 ** 5

if len(cam_list) == 0:
    print(board_size)
    exit()
use_cam(0)

print(answer)