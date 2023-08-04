import sys
from collections import deque

h, k, r = map(int, input().split())

works = []

for _ in range(2**h):
    works.append(deque(map(int, input().split())))

worker_num = 2**(h+1)-1
company = [deque() for _ in range(worker_num)]

flag = 0

def find_boss(num):
    return (num-1) // 2

for i in range(1, 2**h+1):
    company[-i] = works[-i]

answer = 0
for day in range(r):
    flag = day % 2
    for i in range(worker_num):
        if len(company[i]) == 0: continue
        elif flag == 1 and len(company[i]) > 1:
            temp = company[i].popleft()
            if i == 0: answer += company[i].popleft()
            else: company[find_boss(i)].append(company[i].popleft())
            company[i].appendleft(temp)
        else:
            if i == 0: answer += company[i].popleft()
            else: company[find_boss(i)].append(company[i].popleft())

print(answer)