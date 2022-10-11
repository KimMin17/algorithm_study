from collections import deque

def bfs(arr, visited, r, c):
    q = deque()
    gap = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q.append((r, c))
    visited[r][c] = True

    while q:
        cur = q.popleft()
        for item in gap:
            c_r = cur[0] + item[0]
            c_c = cur[1] + item[1]

            if arr[c_r][c_c] == 1 and visited[c_r][c_c] == False:
                q.append((c_r, c_c))
                visited[c_r][c_c] = True

def solution():
    m, n, k = tuple(map(int, input().split(" ")))

    arr = [[0 for j in range(n+2)] for i in range(m+2)]
    visited = [[False for j in range(n+2)] for i in range(m+2)]
    l = []

    for i in range(k):
        r, c = tuple(map(int, input().split(" ")))
        arr[r+1][c+1] = 1
        l.append((r+1, c+1))

    count = 0
    for cord in l:
        if visited[cord[0]][cord[1]] is False:
            count += 1
            bfs(arr, visited, cord[0], cord[1])
    return count

test_case = int(input())
results = []
for i in range(test_case):
    results.append(solution())

for result in results:
    print(result)