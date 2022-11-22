import sys

vertex_num = int(input())
edge_num = int(input())

MAX = sys.maxsize

conn = [[MAX] * vertex_num for _ in range(vertex_num)]

for _ in range(edge_num):
    dept, dest, cost = tuple(map(int, sys.stdin.readline().split()))
    conn[dept-1][dest-1] = min(cost, conn[dept-1][dest-1])

for k in range(vertex_num):
    for i in range(vertex_num):
        for j in range(vertex_num):
            conn[i][j] = min(conn[i][j], conn[i][k] + conn[k][j])

for i in range(vertex_num): conn[i][i] = 0

for i in range(vertex_num):
    for j in range(vertex_num):
        if conn[i][j] == MAX: conn[i][j] = 0

for item in conn:
    print(*item)