import sys

input = sys.stdin.readline

def check_done(arr, i, j, num):
    for k in range(9):
        if num == arr[i][k]: return False
    
    for k in range(9):
        if num == arr[k][j]: return False

    block_i = (i // 3) * 3
    block_j = (j // 3) * 3

    for k in range(3):
        for l in range(3):
            if num == arr[block_i + k][block_j + l]: return False

    return True

def find_blank(arr):
    blank_list = []
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0: 
                blank_list.append((i, j))
    return blank_list

def dfs(step):
    if step == len(blank_list):
        for line in sudoku:
            print(*line)
        exit()
    else:
        i, j = blank_list[step]
        
        for num in range(1, 10):
            if check_done(sudoku, i, j, num):
                sudoku[i][j] = num
                dfs(step + 1)
                sudoku[i][j] = 0

sudoku = []

for _ in range(9):
    sudoku.append(list(map(int, input().split())))

blank_list = find_blank(sudoku)

dfs(0)