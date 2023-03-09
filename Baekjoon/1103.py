n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input()))

answer = 0
visited = [[False] * m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
gaps = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check(i, j):
    if 0 <= i < n and 0 <= j < m:
        if board[i][j] != "H": return True
    return False

def solve(i, j, step):
    global answer
    if dp[i][j] != -1: return dp[i][j]
    max_val = 0
    walk = int(board[i][j])

    visited[i][j] = True
    answer = max(step, answer)
    for gap in gaps:
        next_i = i + walk * gap[0]
        next_j = j + walk * gap[1]
        if check(next_i, next_j):
            if not visited[next_i][next_j]:
                max_val = max(max_val, solve(next_i, next_j, step + 1))
            else:
                print(-1)
                exit()
    answer = max(answer, step + max_val)
    dp[i][j] = max_val + 1

    visited[i][j] = False
    return dp[i][j]

solve(0, 0, 1)

print(answer)