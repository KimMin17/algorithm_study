scroll = list(input())

bridge = []

bridge.append(list(input()))
bridge.append(list(input()))

bri_len = len(bridge[0])
scroll_len = len(scroll)

dp = [[[-1, -1] for _ in range(bri_len)] for _ in range(scroll_len)]

ANGEL = 0
DEVIL = 1

def dfs(step, bri_loc, flag):
    if dp[step][bri_loc][flag] != -1: return dp[step][bri_loc][flag]
    if step == scroll_len - 1: return 1

    total = 0
    next_flag = (flag+1)%2

    for i in range(bri_loc+1, bri_len):
        if bridge[next_flag][i] == scroll[step+1]:
            total += dfs(step+1, i, next_flag)

    dp[step][bri_loc][flag] = total
    return total

answer = 0

for i in range(bri_len):
    if bridge[ANGEL][i] == scroll[0]: answer += dfs(0, i, ANGEL)
    if bridge[DEVIL][i] == scroll[0]: answer += dfs(0, i, DEVIL)

print(answer)