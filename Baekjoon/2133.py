n = int(input())

if n % 2 == 1:
    print(0)
    exit()

answer = 0
n //= 2

if n == 1:
    print(3)
    exit()

def dfs(length, case_num):
    if length == n:
        return case_num

    case_sum = 0
    case_sum += dfs(length+1, case_num*3)
    for i in range(2, n):
        if length + i <= n:
            case_sum += dfs(length+i, case_num*2)
    
    return case_sum

answer += dfs(0, 1)
answer += 2

print(answer)