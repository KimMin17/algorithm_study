n = int(input())

infos = []

for _ in range(n):
    infos.append(list(map(int, input().split())))

build_seq = []

dp = [0] * n

for info in infos:
    build_seq.append(info[1:-1])

def solve(build_num):
    if dp[build_num] != 0: return dp[build_num]
    pre_time = 0
    for s in build_seq[build_num]:
        pre_time = max(pre_time, solve(s-1))
    dp[build_num] = infos[build_num][0] + pre_time
    return dp[build_num]

for i in range(n):
    print(solve(i))