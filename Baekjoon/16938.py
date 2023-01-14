n, l, r, x = map(int, input().split())

problems = list(map(int, input().split()))

idx = (1 << n) - 1

def solve(idx):
    total = 0
    start = 1
    min_p = 98765432
    max_p = 0

    for i in range(n):
        if idx & start != 0:
            total += problems[i]
            if total > r: return 0
            max_p = max(max_p, problems[i])
            min_p = min(min_p, problems[i])
        start = start << 1

    if max_p - min_p < x: return 0
    if total < l: return 0
    else: return 1

answer = 0
while idx > 0:
    answer += solve(idx)
    idx -= 1

print(answer)