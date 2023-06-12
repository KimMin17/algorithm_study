'''
YYYYY
SYSYS
YYYYY
YSYYS
YYYYY
'''

from itertools import combinations
from collections import deque

graph = []

for _ in range(5):
    graph.append(list(input()))

answers = []

def range_check(i, j):
    if 0 <= i < 5 and 0 <= j < 5: return True
    else: return False

gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def conv_loc(num):
    return (num // 5, num % 5)

def conv_num(i, j):
    return  i * 5 + j

target_list = combinations(range(25), 7)

answer = 0

def is_connected(target):
    node_num = 1
    q = deque()
    visited = [False] * 25

    q.append(conv_loc(target[0]))
    visited[target[0]] = True

    while q:
        cur_i, cur_j = q.popleft()
        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]
            if range_check(next_i, next_j):
                next_num = conv_num(next_i, next_j)
                if next_num in target and not visited[next_num]:
                    q.append((next_i, next_j))
                    visited[next_num] = True
                    node_num += 1

    if node_num == 7: return True
    else: return False

def solve(target):
    global answer
    y_num = 0
    for t in target:
        i, j = conv_loc(t)
        if graph[i][j] == 'Y': y_num += 1
    if y_num > 3: return
    if not is_connected(target): return
    answer += 1

for target in target_list:
    solve(target)

print(answer)