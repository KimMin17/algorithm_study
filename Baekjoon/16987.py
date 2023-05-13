'''
3
1 100
8 5
3 5
'''

n = int(input())

eggs = []

for _ in range(n):
    eggs.append(list(map(int, input().split())))

def is_broken(egg_num):
    if eggs[egg_num][0] <= 0: return True
    else: return False

def crash(egg1, egg2):
    eggs[egg1][0] -= eggs[egg2][1]
    eggs[egg2][0] -= eggs[egg1][1]
    result = 0
    if is_broken(egg1): result += 1
    if is_broken(egg2): result += 1
    return result

def undo(egg1, egg2):
    eggs[egg1][0] += eggs[egg2][1]
    eggs[egg2][0] += eggs[egg1][1]

answer = 0

def dfs(cur_egg, broken_num):
    global answer
    if cur_egg == n:
        answer = max(answer, broken_num)
    elif is_broken(cur_egg):
        dfs(cur_egg+1, broken_num)
    else:
        for next_egg in range(n):
            if next_egg == cur_egg or is_broken(next_egg): continue
            new_broken = crash(cur_egg, next_egg)
            answer = max(answer, broken_num+new_broken)
            dfs(cur_egg+1, broken_num+new_broken)
            undo(cur_egg, next_egg)

dfs(0, 0)
print(answer)