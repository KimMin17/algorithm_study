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
    if eggs[egg1][0] <= 0:
        result += 1
    if eggs[egg2][0] <= 0:
        result += 1
    return result

def undo(egg1, egg2):
    eggs[egg1][0] += eggs[egg2][1]
    eggs[egg2][0] += eggs[egg1][1]

answer = 0
def dfs(egg_num, broken_egg_num):
    global answer
    if egg_num == n:
        answer = max(answer, broken_egg_num)
        return
    
    if is_broken(egg_num):
        dfs(egg_num+1, broken_egg_num)

    for i in range(n):
        if i == egg_num or is_broken(i): continue
        result = crash(egg_num, i)
        dfs(egg_num + 1, broken_egg_num + result)
        undo(egg_num, i)

dfs(0, 0)
print(answer)