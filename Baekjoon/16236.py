from collections import deque

n = int(input())

sea = []

for _ in range(n):
    sea.append(list(map(int,input().split())))

shark_size = 2
shark_count = 0

def find_shark():
    global n
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sea[i][j] = 0
                return i, j

shark_i, shark_j = find_shark()

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dist = [[-1] * n for _ in range(n)]

def calc_dist(s_i, s_j):
    global dist
    for i in range(n):
        for j in range(n):
            dist[i][j] = -1

    q = deque()
    visited = [[False] * n for _ in range(n)]

    q.append((s_i, s_j, 0))
    visited[s_i][s_j] = True

    while q:
        cur_i, cur_j, cur_dist = q.popleft()
        dist[cur_i][cur_j] = cur_dist
        for gap in gaps:
            next_i, next_j = cur_i + gap[0], cur_j + gap[1]
            if check_range(next_i, next_j):
                if not visited[next_i][next_j] and sea[next_i][next_j] <= shark_size:
                    q.append((next_i, next_j, cur_dist+1))
                    visited[next_i][next_j] = True

def find_target():
    target_loc = []
    for i in range(n):
        for j in range(n):
            if 0 < sea[i][j] < shark_size:
                target_loc.append((i, j))
    target_loc.sort()

    calc_dist(shark_i, shark_j)

    min_dist = 10000
    final_i, final_j = -1, -1
    for t_i, t_j in target_loc:
        new_dist = dist[t_i][t_j]
        if new_dist == -1: continue
        if new_dist < min_dist:
            min_dist = new_dist
            final_i, final_j = t_i, t_j
    
    return final_i, final_j

def check_range(i, j):
    if 0 <= i < n and 0 <= j < n: return True
    return False

answer = 0
while True:
    target_i, target_j = find_target()
    if target_i == -1 and target_j == -1: break
    answer += dist[target_i][target_j]
    shark_i, shark_j = target_i, target_j
    shark_count += 1
    if shark_count == shark_size:
        shark_size += 1
        shark_count = 0
    sea[target_i][target_j] = 0

print(answer)