from collections import deque

n = int(input())

board = []

for _ in range(n):
    board.append(list(input()))

def range_check(i, j):
    if 0 <= i < n and 0 <= j < n: return True
    else: return False

gaps = [[1, 0], [0, -1], [-1, 0], [0, 1]]
def bfs(start_i, start_j, visited):
    q = deque()
    q.append((start_i, start_j))
    visited[start_i][start_j] = True
    color = board[start_i][start_j]

    while q:
        cur_i, cur_j = q.popleft()
        for gap in gaps:
            next_i = cur_i + gap[0]
            next_j = cur_j + gap[1]
            if range_check(next_i, next_j):
                if not visited[next_i][next_j] and board[next_i][next_j] == color:
                    visited[next_i][next_j] = True
                    q.append((next_i, next_j))

def find_not_visited(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False: return (i, j)

    return (-1, -1)

def solve():
    visited = [[False] * n for _ in range(n)]
    answer = 0

    start_i, start_j = find_not_visited(visited)
    while start_i != -1 and start_j != -1:
        bfs(start_i, start_j, visited)
        answer += 1
        start_i, start_j = find_not_visited(visited)
    
    return answer

def change_color():
    for i in range(n):
        for j in range(n):
            if board[i][j] == "G": board[i][j] = "R"

answer1 = solve()
change_color()
answer2 = solve()

print(answer1, answer2)