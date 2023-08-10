from copy import deepcopy

n = int(input())

balls = list(input())

def insert(color, l):
    result = 0
    flag = True
    if l[0] != color: flag = False

    idx = 0
    if flag:
        while idx < n:
            if l[idx] != color: break
            idx += 1
    
    while idx < n:
        if l[idx] == color: result += 1
        idx += 1
    return result

answer = insert("R", balls)
answer = min(answer, insert("B", balls))

balls_reversed = deepcopy(balls)
balls_reversed.reverse()

answer = min(answer, insert("R", balls_reversed))
answer = min(answer, insert("B", balls_reversed))

print(answer)