'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''

from collections import deque

R = 0
D = 1
L = 2
U = 3

gap = [[0, 1], [1, 0], [0, -1], [-1, 0]]

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

mov_n = int(input())
mov_list = deque()

for _ in range(mov_n):
    rot_time, rot = tuple(input().split())
    mov_list.append((int(rot_time), rot))

def turn(cur_dir, rot):
    if rot == "L":
        return int((cur_dir + 3) % 4)
    elif rot == "D":
        return int((cur_dir + 1) % 4)

def check_game_over(i, j):
    global n
    if (i, j) in snake: return True
    if i < 0 or i >= n or j < 0 or j >= n: return True
    return False

def move_snake():
    global time
    global direction

    head_i, head_j = snake[0]
    next_i = head_i+gap[direction][0]
    next_j = head_j+gap[direction][1]
    if check_game_over(next_i, next_j):
        print(time+1)
        exit()

    next_loc = (next_i, next_j)
    snake.appendleft(next_loc)
    if board[next_i][next_j] == 1:
        board[i][j] = 0
    else:
        tail_i, tail_j = snake.pop()
        board[tail_i][tail_j] = 0

time = 0
direction = R

snake = deque()
snake.appendleft((0, 0))

while True:
    move_snake()
    time += 1
    if len(mov_list) > 0:
        rot_time, rot = mov_list[0]
        if time == rot_time:
            direction = turn(direction, rot)
            mov_list.popleft()