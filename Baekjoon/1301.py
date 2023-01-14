n = int(input())

if n < 3:
    print(0)
    exit()

biz = []

for _ in range(n):
    biz.append(int(input()))

biz_sum = sum(biz)

dp = {}

def encoder(code):
    key = ".".join(list(map(str, code)))
    return key

def solve(step, last, cur):
    if step == biz_sum: return 1
    
    key = encoder([*biz, last, cur])

    if key in dp:
        return dp[key]
    else:
        result = 0
        for i in range(1, n+1):
            if i != last and i != cur and biz[i-1] != 0:
                biz[i-1] -= 1
                result += solve(step + 1, cur, i)
                biz[i-1] += 1
        dp[key] = result
        return result

print(solve(0, 0, 0))