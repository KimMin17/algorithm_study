import sys
from collections import deque

input = sys.stdin.readline

n, w = tuple(map(int, input().split()))

node_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = tuple(map(int, input().split()))
    node_list[a].append(b)
    node_list[b].append(a)

q = deque()
visited = [False] * (n+1)

q.append(1)
visited[1] = True

leaf_count = 0

while q:
    cur = q.popleft()
    is_leaf = True

    for child in node_list[cur]:
        if visited[child] == True: continue
        q.append(child)
        visited[child] = True
        is_leaf = False
    
    if is_leaf: leaf_count += 1

print("{:.6f}".format(w / leaf_count))