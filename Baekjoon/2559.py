from collections import deque

n, k = map(int, input().split())

vals = list(map(int, input().split()))

q = deque()

total = 0

for i in range(k):
    total += vals[i]

answer = total

for i in range(k, n):
    total += vals[i]
    total -= vals[i-k]
    answer = max(answer, total)

print(answer)