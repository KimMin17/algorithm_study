from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

ice_list = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0: ice_list.append((i, j))

ice_num = len(ice_list)

def find_ice():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0: return (i, j)
    return (-1, -1)
    
def melt_ice():
    melt_list = []
    gaps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    while ice_list:
        i, j = ice_list.popleft()
        melt_count = 0
        for gap in gaps:
            next_i = i + gap[0]
            next_j = j + gap[1]
            if graph[next_i][next_j] == 0: melt_count += 1
        melt_list.append((i, j, melt_count))

    for melt in melt_list:
        i, j, melt_count = melt
        graph[i][j] -= melt_count
        if graph[i][j] > 0: ice_list.append((i, j))
        else: graph[i][j] = 0
    return len(ice_list)

def bfs(s_i, s_j):
    q = deque()
    visited = [[False] * m for _ in range(n)]

    gaps = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q.append((s_i, s_j))
    visited[s_i][s_j] = True
    count = 0

    while q:
        cur_i, cur_j = q.popleft()
        count += 1
        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]
            if graph[next_i][next_j] != 0 and not visited[next_i][next_j]:
                q.append((next_i, next_j))
                visited[next_i][next_j] = True

    return count

year = 0
while True:
    year += 1
    ice_num = melt_ice()

    s_i, s_j = find_ice()
    if s_i == -1 and s_j == -1:
        print('0')
        break

    ice_left = bfs(s_i, s_j)
    if ice_left != ice_num:
        print(year)
        break