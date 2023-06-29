n = int(input())

cur_light = list(map(int, input()))
target_light = list(map(int, input()))

temp_light = [cur_light[i] for i in range(n)]

def change_light(i):
    global n
    if 0 <= i-1 < n:
        cur_light[i-1] += 1
        cur_light[i-1] %= 2
    if 0 <= i < n:
        cur_light[i] += 1
        cur_light[i] %= 2
    if 0 <= i+1 < n:
        cur_light[i+1] += 1
        cur_light[i+1] %= 2
    
answer = 0
for i in range(0, n-1):
    if cur_light[i] != target_light[i]:
        change_light(i+1)
        answer += 1

for i in range(n):
    if cur_light[i] != target_light[i]:
        answer = -1
        break

if answer != -1:
    print(answer)
    exit()

another_answer = 1
cur_light = [temp_light[i] for i in range(n)]
change_light(0)

for i in range(0, n-1):
    if cur_light[i] != target_light[i]:
        change_light(i+1)
        another_answer += 1

for i in range(n):
    if cur_light[i] != target_light[i]:
        another_answer = -1
        break
print(another_answer)