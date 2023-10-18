n = int(input())

house_cost = []

for _ in range(n):
    house_cost.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]

for i in range(3):
    dp[0][i] = house_cost[0][i]

def dfs(loc, color):
    if dp[loc][color] != 0: return dp[loc][color]

    dp[loc][color] = min(dfs(loc-1, (color+1)%3), dfs(loc-1, (color+2)%3)) + house_cost[loc][color]
    return dp[loc][color]


print(min(dfs(n-1, 0), dfs(n-1, 1), dfs(n-1, 2)))