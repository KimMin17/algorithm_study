from collections import deque

r, c = map(int, input().split())

board = []

INNER_AIR = 0
OUTER_AIR = 8

for _ in range(r):
    board.append(list(map(int, input().split())))

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def range_check(i, j):
    if 0 <= i < r and 0 <= j < c: return True
    return False

def bfs(start_i, start_j):
    air_type = board[start_i][start_j]

    q = deque()
    air_list = deque()
    visited = [[False] * c for _ in range(r)]

    q.append((start_i, start_j))
    air_list.append((start_i, start_j))
    visited[start_i][start_j] = True
    while q:
        cur_i, cur_j = q.popleft()
        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]

            if range_check(next_i, next_j):
                if board[next_i][next_j] == air_type and not visited[next_i][next_j]:
                    visited[next_i][next_j] = True
                    air_list.append((next_i, next_j))
                    q.append((next_i, next_j))
    
    return air_list

def find_inner_air_list():
    inner_air_list = deque()
    visited = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] == INNER_AIR and not visited[i][j]:
                inner_air = bfs(i, j)
                for air in inner_air:
                    visited[air[0]][air[1]] = True
                inner_air_list.append(inner_air)
    
    return inner_air_list

def change_air(air_type, air_list):
    for air in air_list:
        i, j = air
        board[i][j] = air_type

outer_air = bfs(0, 0)
inner_air_list = find_inner_air_list()
change_air(OUTER_AIR, outer_air)

cheese_list = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 1:
            cheese_list.append((i, j))

def melt_cheese():
    melt_list = deque()
    cheese_len = len(cheese_list)
    for _ in range(cheese_len):
        i, j = cheese_list.popleft()
        outer_air_count = 0
        for gap in gaps:
            next_i = i + gap[0]
            next_j = j + gap[1]
            if board[next_i][next_j] == OUTER_AIR:
                outer_air_count += 1
        if outer_air_count >= 2:
            melt_list.append((i, j))
        else: cheese_list.append((i, j))

    for i, j in melt_list:
        board[i][j] = OUTER_AIR

def check_inner_air():
    inner_air_len = len(inner_air_list)
    for _ in range(inner_air_len):
        inner_air = inner_air_list.popleft()
        changed = False
        for air in inner_air:
            for gap in gaps:
                if board[air[0]+gap[0]][air[1]+gap[1]] == OUTER_AIR:
                    change_air(OUTER_AIR, inner_air)
                    changed = True
                    break
            if changed: break
        if not changed:
            inner_air_list.append(inner_air)

counter = 0
while True:
    melt_cheese()
    check_inner_air()
    counter += 1
    if len(cheese_list) == 0: break

print(counter)