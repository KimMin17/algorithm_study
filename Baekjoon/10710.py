n, m = map(int, input().split())

dist = []
weather = []

dp = [[0] * m for _ in range(n)]

for _ in range(n):
    dist.append(int(input()))

for _ in range(m):
    weather.append(int(input()))

INF = 10**9

def solve(step, day):
    if step < 0:
        return 0
    if step > day:
        dp[step][day] = INF
        return INF
    if dp[step][day] != 0: return dp[step][day]

    choice1 = solve(step-1, day-1) + dist[step] * weather[day]
    choice2 = solve(step, day-1)

    dp[step][day] = min(choice1, choice2)

    return dp[step][day]

for i in range(m):
    solve(n-1, i)

answer = min(dp[n-1])
print(answer)