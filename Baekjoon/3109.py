'''
5 5
.xx..
..x..
.....
...x.
...x.
'''

r, c = map(int, input().split())

board = []

route = [[0] * c for _ in range(r)]

for _ in range(r):
    board.append(list(input()))

def check_range(i, j):
    if 0 <= i < r and 0 <= j < c: return True
    return False

gaps = [[1, -1], [0, -1], [-1, -1]]
