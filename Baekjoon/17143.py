r, c, m = map(int, input().split())

sea = [[-1] * c for _ in range(r)]
sharks = []

for i in range(m):
    s_i, s_j, s, d, z = map(int, input().split())
    sea[s_i-1][s_j-1] = i
    sharks.append([s, d-1, z, s_i-1, s_j-1, True, i])

SPEED = 0
DIR = 1
SIZE = 2
I_LOC = 3
J_LOC = 4
IS_ALIVE = 5
SHARK_ID = 6

directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def fish(loc):
    shark_size = 0
    for i in range(r):
        if sea[i][loc] != -1 and sharks[sea[i][loc]][IS_ALIVE]:
            shark_size = sharks[sea[i][loc]][SIZE]
            sharks[sea[i][loc]][IS_ALIVE] = False
            sea[i][loc] = -1
            break
    return shark_size

def calc_next_loc(shark):
    d = shark[DIR]
    i, j = shark[I_LOC], shark[J_LOC]
    if d < 2: # move up-down
        for _ in range(shark[SPEED]%((r-2)*2+2)):
            if i == 0 and d == 0: d = 1
            elif i == r-1 and d == 1: d = 0
            i += directions[d][0]
    else: # move left-right
        for _ in range(shark[SPEED]%((c-2)*2+2)):
            if j == 0 and d == 3: d = 2
            elif j == c-1 and d == 2: d = 3
            j += directions[d][1]

    shark[I_LOC] = i
    shark[J_LOC] = j
    shark[DIR] = d

def move_shark():
    for shark in sharks:
        if not shark[IS_ALIVE]: continue
        cur_i, cur_j = shark[I_LOC], shark[J_LOC]
        sea[cur_i][cur_j] = -1
        calc_next_loc(shark)

    for shark in sharks:
        if not shark[IS_ALIVE]: continue
        next_i, next_j = shark[I_LOC], shark[J_LOC]
        if sea[next_i][next_j] == -1: sea[next_i][next_j] = shark[SHARK_ID]
        else:
            another_shark_id = sea[next_i][next_j]
            if sharks[another_shark_id][SIZE] > shark[SIZE]:
                shark[IS_ALIVE] = False
            else:
                sharks[another_shark_id][IS_ALIVE] = False
                sea[next_i][next_j] = shark[SHARK_ID]

answer = 0
for i in range(c):
    answer += fish(i)
    move_shark()

print(answer)