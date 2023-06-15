from collections import deque

n = int(input())

works = []

for _ in range(n):
    works.append(tuple(map(int, input().split())))

s = deque()

answer = 0
for work in works:
    if len(work) != 1:
        _, new_score, new_time = work
        s.append((new_score, new_time))
    
    if len(s) == 0: continue

    score, time = s.pop()
    if time == 1: answer += score
    else: s.append((score, time-1))

print(answer)