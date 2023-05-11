from collections import deque

INF = 10**9 + 1

n = int(input())

if n == 1:
    print(0)
    exit()

arr = []

for _ in range(n):
    arr.append(int(input()))

max_val = max(arr)

s = deque()
answer = 0

for num in arr:
    if not s: s.append(num)
    else:
        if s[-1] < num:
            answer += (num - s.pop())
            s.append(num)
        elif s[-1] > num:
            s.pop()
            s.append(num)

while s:
    answer += (max_val - s.pop())

print(answer)