n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

gaps = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]] 

def dfs(go_num):
    if go_num == 1:
        print("Possible")
        exit()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                for gap in gaps:
                    if board[i+gap[0]][j+gap[1]] == 2 and board[i+2*gap[0]][j+2*gap[1]] == 0:
                        board[i][j] = 0
                        board[i+gap[0]][j+gap[1]] = 0
                        board[i+2*gap[0]][j+2*gap[1]] = 2
                        dfs(go_num-1)
                        board[i][j] = 2
                        board[i+gap[0]][j+gap[1]] = 2
                        board[i+2*gap[0]][j+2*gap[1]] = 0
    
go_num = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2: go_num += 1

dfs(go_num)
print("Impossible")