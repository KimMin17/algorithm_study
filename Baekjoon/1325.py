n, m = tuple(map(int, input().split(" ")))

conn = [[] for i in range(n+1)]

for i in range(m):
    a, b = tuple(map(int, input().split(" ")))
    conn[b].append(a)

