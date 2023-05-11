'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''
from itertools import combinations

n, m = map(int, input().split())

INF = 10**9

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

house_to_chicken = [[] for _ in range(len(house))]

for i in range(len(house)):
    for c in chicken:
        d = abs(house[i][0] - c[0]) + abs(house[i][1] - c[1])
        house_to_chicken[i].append(d)

chosen_c_list = combinations(range(len(chicken)), m)

def get_c_dist(c_list):
    c_dist = 0
    for i in range(len(house)):
        target_dist = INF
        for c in c_list:
            target_dist = min(target_dist, house_to_chicken[i][c])
        c_dist += target_dist
    return c_dist

answer = INF

for chosen_c in chosen_c_list:
    answer = min(answer, get_c_dist(chosen_c))

print(answer)