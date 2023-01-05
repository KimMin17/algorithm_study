MAX = 987654321

n = int(input())

arr = []
dp = [[-1] * (1 << n) for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

def dfs(cur, visit):
    if visit == (1 << n) - 1:
        if arr[cur][0] != 0:
            dp[cur][visit] = arr[cur][0]
            return arr[cur][0]
        else: return MAX

    if dp[cur][visit] != -1:
        return dp[cur][visit]
    
    min_dist = MAX
    for i in range(1, n):
        if arr[cur][i] == 0: continue
        if visit & (1 << i) != 0: continue
        
        min_dist = min(min_dist, dfs(i, visit | (1 << i)) + arr[cur][i])
    
    dp[cur][visit] = min_dist
    return dp[cur][visit]

print(dfs(0, 1))