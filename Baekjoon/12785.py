c, r = tuple(map(int, input().split()))
loc_c, loc_r = tuple(map(int, input().split()))

mod = 1000007

def solve(r, c):
    board = [[1] * c for _ in range(r)]
    for i in range(1, r):
        for j in range(1, c):
            board[i][j] = int((board[i-1][j]+board[i][j-1]) % mod)
    return board[r-1][c-1]

print(int(solve(loc_r, loc_c) * solve(r-loc_r+1, c-loc_c+1) % mod))