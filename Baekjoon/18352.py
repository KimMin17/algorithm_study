from collections import deque

n, m, k, x = tuple(map(int, input().split(" ")))

conn = [[] for _ in range(n)]

for _ in range(m):
    depart, dest = tuple(map(int, input().split(" ")))
    conn(depart).append(dest)

