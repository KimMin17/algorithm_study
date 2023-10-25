n = int(input())

dp = [0] * (n+1)

def dfs(i):
    if dp[i] != 0: return dp[i]
    if i == 0: return 0

    if i >= 5:
        choice1 = dfs(i-3)
        choice2 = dfs(i-5)

        if choice1 == -1 and choice2 == -1: dp[i] = -1
        elif choice1 == -1: dp[i] = choice2 + 1
        elif choice2 == -1: dp[i] = choice1 + 1
        else:
            dp[i] = min(choice1, choice2) + 1
    elif i >= 3:
        choice1 = dfs(i-3)
        if choice1 == -1: dp[i] = -1
        else: dp[i] = choice1 + 1

    else: dp[i] = -1

    return dp[i]

print(dfs(n))