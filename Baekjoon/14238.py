from collections import deque

record = input()
shifts = [0, 0, 0]

shift_size = len(record)

for i in record:
    if i == "A": shifts[0] += 1
    elif i == "B": shifts[1] += 1
    else: shifts[2] += 1

def encoder(arr):
    return ".".join(str(arr))

dp = {}
s = deque()

def print_stack(s):
    while s:
        print(s.popleft(), end="")

def solution(step, last, cur):
    if step == shift_size:
        print_stack(s)
        exit()
    
    key = encoder([*shifts, last, cur])

    if key in dp:
        return dp[key]
    
    able = False
    for i in range(3):
        if i == 0 and shifts[0] > 0:
            shifts[0] -= 1
            s.append("A")
            able = able or solution(step+1, cur, i)
            shifts[0] += 1
            s.pop()

        if i == 1 and cur != 1 and shifts[1] > 0:
            shifts[1] -= 1
            s.append("B")
            able = able or solution(step+1, cur, i)
            shifts[1] += 1
            s.pop()

        if i == 2 and cur != 2 and last != 2 and shifts[2] > 0:
            shifts[2] -= 1
            s.append("C")
            able = able or solution(step+1, cur, i)
            shifts[2] += 1
            s.pop()
        
    if not able: dp[key] = False
    else: dp[key] = True
    return dp[key]

if not solution(0 ,-1, -1): print(-1)