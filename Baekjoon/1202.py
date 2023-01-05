import sys, heapq

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))

j = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(k)]

j.sort()
b.sort()

answer = 0
tmp = []

for _ in range(k):
    cur_bag = heapq.heappop(b)
    while j and j[0][0] <= cur_bag:
        heapq.heappush(tmp, -1 * heapq.heappop(j)[1])    
    if tmp:
        answer += (heapq.heappop(tmp) * -1)

print(answer)