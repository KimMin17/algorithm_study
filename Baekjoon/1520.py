'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''

n, m = map(int, input().split())

graph = []
dp = [[-1] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

gaps = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def range_check(i, j):
    if 0 <= i < n and 0 <= j < m: return True
    else: return False

def dfs(i, j):
    if dp[i][j] != -1: return dp[i][j]
    if i == n-1 and j == m-1:
        return 1
    
    route_num = 0
    for gap in gaps:
        next_i = i + gap[0]
        next_j = j + gap[1]
        if range_check(next_i, next_j):
            if graph[i][j] > graph[next_i][next_j]:
                route_num += dfs(next_i, next_j)

    dp[i][j] = route_num
    return route_num

print(dfs(0, 0))