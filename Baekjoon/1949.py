from collections import deque
import sys

sys.setrecursionlimit(10**5)

n = int(input())

vil_list = list(map(int, input().split()))
vil_list.insert(0, 0)

conn = [[] for _ in range(n+1)]

for _ in range(n-1):
    vil1, vil2 = map(int, input().split())
    conn[vil1].append(vil2)
    conn[vil2].append(vil1)

dp = [[0, 0] for _ in range(n+1)]

F = 0
T = 1

def dfs(cur_vil, flag, before):
    if dp[cur_vil][flag] != 0: return dp[cur_vil][flag]

    result = 0
    if flag == F:
        for next_vil in conn[cur_vil]:
            if next_vil == before: continue
            result += max(dfs(next_vil, F, cur_vil), dfs(next_vil, T, cur_vil))
    else:
        result += vil_list[cur_vil]
        for next_vil in conn[cur_vil]:
            if next_vil == before: continue
            result += dfs(next_vil, F, cur_vil)
    
    dp[cur_vil][flag] = result
    return result

print(max(dfs(1, T, 0), dfs(1, F, 0)))