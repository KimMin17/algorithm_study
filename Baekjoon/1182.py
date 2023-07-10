from itertools import combinations

n, s = map(int, input().split())

nums = list(map(int, input().split()))

answer = 0
for i in range(1, n+1):
    combs = combinations(nums, i)
    for comb in combs:
        if sum(comb) == s: answer += 1

print(answer)