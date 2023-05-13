'''
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6
'''

n = int(input())

works = [[0, 0]]

for _ in range(n):
    works.append(list(map(int, input().split())))

n += 1

dp = [0] * n
seq = [[] for _ in range(n)]

for i in range(len(works)):
    if len(works[i]) == 2: continue
    for j in range(2, len(works[i])):
        seq[i].append(works[i][j])

def get_time(work_num): return works[work_num][0]

for i in range(n):
    max_pre_time = 0
    for s in seq[i]:
        max_pre_time = max(max_pre_time, dp[s])
    dp[i] = max(dp[i], get_time(i) + max_pre_time)

print(max(dp))