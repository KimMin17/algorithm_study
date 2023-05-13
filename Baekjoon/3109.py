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

gaps = [[-1, -1], [0, -1], [1, -1]]

answer = 0

def dfs(cur_i, cur_j):
    global answer
    global search_done

    if cur_j == 0:
        search_done = True
        answer += 1
        return
    
    for gap in gaps:
        next_i = cur_i + gap[0]
        next_j = cur_j + gap[1]

        if not check_range(next_i, next_j): continue
        if board[next_i][next_j] == ".":
            board[next_i][next_j] = "O"
            dfs(next_i, next_j)
            if search_done: return

search_done = False
for i in range(r):
    search_done = False
    dfs(i, c-1)
    
print(answer)