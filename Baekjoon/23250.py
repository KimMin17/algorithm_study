n, k = map(int, input().split())

step_counter = 0

dp = [-1] * (n+1)
dp[1] = 1

def solve(n, start, end, mid):
    global step_counter
    global dp
    if dp[n] != -1 and step_counter + dp[n] < k:
        step_counter += dp[n]
        return
    if n == 1:
        step_counter += 1
        if step_counter == k:
            print(start, end)
            exit()
        pass
    else:
        solve(n-1, start, mid, end)
        step_counter += 1
        if step_counter == k:
            print(start, end)
            exit()
        solve(n-1, mid, end, start)
        if dp[n] == -1: dp[n] = step_counter

solve(n, 1, 3, 2)