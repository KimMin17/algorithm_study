from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())

room = []
answer = 0

for _ in range(n):
    room.append(list(input().replace(" ", "")))

build_locs = []
virus_locs = []

for i in range(n):
    for j in range(m):
        if room[i][j] == '2': virus_locs.append((i, j))

def check_range(i, j):
    if 0 <= i < n and 0 <= j < m: return True
    else: return False

def virus_spread(experiment):
    gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    q = deque(virus_locs)

    while q:
        cur_i, cur_j = q.popleft()
        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]
            if check_range(next_i, next_j):
                if experiment[next_i][next_j] == '0':
                    experiment[next_i][next_j] = '2'
                    q.append((next_i, next_j))

for i in range(n):
    for j in range(m):
        if room[i][j] == '0':
            build_locs.append((i, j))

combs = combinations(build_locs, 3)

for comb in combs:
    experiment = deepcopy(room)
    for build in comb:
        experiment[build[0]][build[1]] = '1'
    
    virus_spread(experiment)
    
    safe_count = 0
    for i in range(n):
        for j in range(m):
            if experiment[i][j] == '0': safe_count += 1
    answer = max(answer, safe_count)

print(answer)