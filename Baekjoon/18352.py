from collections import deque

n, m, k, x = tuple(map(int, input().split(" ")))

conn = [[] for _ in range(n + 1)]

for _ in range(m):
    depart, dest = tuple(map(int, input().split(" ")))
    conn[depart].append(dest)

q = deque()
visited = [False for _ in range(n + 1)]

q.append((x, 0))
visited[x] = True

answers = []

while q:
    cur = q.popleft()
    if cur[1] == k:
        answers.append(cur[0])
    for item in conn[cur[0]]:
        if visited[item] == False:
            q.append((item, cur[1] + 1))
            visited[item] = True

if len(answers) == 0:
    print("-1")
else:
    answers.sort()
    for answer in answers:
        print(answer)