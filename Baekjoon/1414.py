import heapq

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

def simple_conv(c):
    if c == '0': return 0
    if c in 'qwertyuiopasdfghjklzxcvbnm': return ord(c) - 96
    if c in 'QWERTYUIOPASDFGHJKLZXCVBNM': return ord(c) - 38

pq = []
total_len = 0

for i in range(n):
    for j in range(n):
        l = simple_conv(graph[i][j])
        total_len += l
        if i == j: continue
        if l != 0: heapq.heappush(pq, (l, i, j))

parent = [i for i in range(n)]

def union(a_parent, b_parent):
    for i in range(n):
        if parent[i] == b_parent: parent[i] = a_parent

def find(n):
    if parent[n] != n: parent[n] = find(parent[n])
    return parent[n]

def check():
    tmp = parent[0]
    for p in parent:
        if tmp != p: return False
    return True

mst_len = 0
while pq:
    l, i, j = heapq.heappop(pq)
    i_parent = find(i)
    j_parent = find(j)

    if i_parent != j_parent:
        mst_len += l
        union(i_parent, j_parent)

    if check(): break

if not check(): print(-1)
else: print(total_len - mst_len)