import sys
from collections import deque

input = sys.stdin.readline

n, w = tuple(map(int, input().split()))

node_list = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c = tuple(map(int, input().split()))
    node_list[p].append(c)

for node in node_list:
    print(*node)

q = deque()
scale = 1
q.append([0, 1 * scale])

p_list = []

while q:
    cur, cur_p = tuple(q.popleft())
    cur_child_num = len(node_list[cur])
    if cur_child_num == 0: p_list.append(cur_p)
    else:
        child_p = cur_p / cur_child_num
        for child in node_list[cur]: q.append([child, child_p])

print(*p_list)