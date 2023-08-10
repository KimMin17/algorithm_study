n, k = map(int, input().split())

dp = [[0, 0, 0] for _ in range(n+1)]

TOTAL = 0
BUN = 1
PATTY = 2

dp[0] = [1, 0, 1]

def dfs(l):
    if dp[l][TOTAL] != 0: return dp[l]
    prior_burger = dfs(l-1)
    dp[l][TOTAL] = 2 * prior_burger[TOTAL] + 3
    dp[l][BUN] = 2 * prior_burger[BUN] + 2
    dp[l][PATTY] = 2 * prior_burger[PATTY] + 1
    return dp[l]

dfs(n)

answer = 0

def check_burger():
    global n, k, answer
    if k == 0:
        print(answer)
        exit()

def eat_burger(level):
    global n, k, answer
    if level == 0:
        k -= 1
        answer += 1
        check_burger()
        return
    if k >= dp[level][TOTAL]:
        k -= dp[level][TOTAL]
        answer += dp[level][PATTY]
        return

    k -= 1
    check_burger()

    eat_burger(level-1)
    check_burger()

    k -= 1
    answer += 1
    check_burger()

    eat_burger(level-1)
    check_burger()

    k -= 1
    check_burger()

eat_burger(n)

print(answer)