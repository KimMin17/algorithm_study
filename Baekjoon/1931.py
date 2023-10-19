n = int(input())

time_list = []
for _ in range(n):
    time_list.append(list(map(int, input().split())))

time_list.sort(key= lambda x : (x[1], x[0]))

answer = 0
cur_time = 0
for t in time_list:
    if cur_time > t[0]: continue
    answer += 1
    cur_time = t[1]

print(answer)