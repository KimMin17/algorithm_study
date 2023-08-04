n = int(input())

times = []
rewards = []

for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    rewards.append(p)

times.append(0)
rewards.append(0)

dp = [0] * (n+1)

def dfs(day):
    if dp[day] != 0: return dp[day]

    max_reward = 0

    for i in reversed(range(day)):
        if times[i] + i <= day:
            max_reward = max(max_reward, dfs(i) + rewards[i])

    dp[day] = max_reward

    return dp[day]

print(dfs(n))