'''
1 8
11911103

3 3
123
456
789

3 1
7
9
3
'''

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))

answer = 0

def get_sum(l, r, u, d):
    total = 0
    for i in range(u, d+1):
        for j in range(l, r+1):
            total += board[i][j]
    return total

# 2v
if m >= 3:
    for i in range(0, m-2):
        for j in range(i+1, m-1):
            answer = max(answer, get_sum(0, i, 0, n-1) * get_sum(i+1, j, 0, n-1) * get_sum(j+1, m-1, 0, n-1))

# 2h

if n >= 3:
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            answer = max(answer, get_sum(0, m-1, 0, i) * get_sum(0, m-1, i+1, j) * get_sum(0, m-1, j+1, n-1))

# 1v l1h
if n >= 2 and m >= 2:
    for i in range(0, n-1):
        for j in range(0, m-1):
            answer = max(answer, get_sum(0, j, 0, i) * get_sum(0, j, i+1, n-1) * get_sum(j+1, m-1, 0, n-1))

# 1v r1h
    for i in range(0, n-1):
        for j in range(0, m-1):
            answer = max(answer, get_sum(0, j, 0, n-1) * get_sum(j+1, m-1, 0, i) * get_sum(j+1, m-1, i+1, n-1))
# 1h u1v
    for i in range(0, n-1):
        for j in range(0, m-1):
            answer = max(answer, get_sum(0, j, 0, i) * get_sum(j+1, m-1, 0, i) * get_sum(0, m-1, i+1, n-1))
# 1h d1v
    for i in range(0, n-1):
        for j in range(0, m-1):
            answer = max(answer, get_sum(0, m-1, 0, i) * get_sum(0, j, i+1, n-1) * get_sum(j+1, m-1, i+1, n-1))

print(answer)