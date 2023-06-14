'''
2 7
2 3 2 3 1 2 7
'''

n, k = map(int, input().split())

use_list = list(map(int, input().split()))

slots = [-1] * n

def schedule(new_use, cur):
    if new_use in slots: return 0
    for i in range(n):
        if slots[i] == -1:
            slots[i] = new_use
            return 0
    next_use = [k] * n
    
    for i in range(n):
        for j in range(cur+1, k):
            if slots[i] == use_list[j]:
                next_use[i] = j
                break
    
    max_idx = 0
    max_val = -1
    for i in range(n):
        if max_val < next_use[i]:
            max_idx = i
            max_val = next_use[i]

    slots[max_idx] = new_use
    return new_use

answer = 0

for i in range(k):
    result = schedule(use_list[i], i)
    if result != 0: answer += 1

print(answer)