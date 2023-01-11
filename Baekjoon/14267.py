from collections import deque

n, m = tuple(map(int, input().split()))

praise = [0] * n
boss = list(map(int, input().split()))

for i in range(1, n):
    boss[i] -= 1

conn = [[] for _ in range(n)]
for i in range(1, n):
    conn[boss[i]].append(i)

for _ in range(m):
    staff, reward = tuple(map(int, input().split()))
    praise[staff - 1] += reward

q = deque()
q.append(0)

while q:
    cur = q.popleft()
    for staff in conn[cur]:
        praise[staff] += praise[cur]
        q.append(staff)

print(*praise)