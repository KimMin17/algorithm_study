from collections import deque

def range_check(loc, chess_range):
    if 0 <= loc[0] < chess_range and 0 <= loc[1] < chess_range: return True
    else: return False

test_case = int(input())

answers = []

for _ in range(test_case):
    chess_range = int(input())
    start_x, start_y = tuple(map(int, input().split(" ")))
    target_x, target_y = tuple(map(int, input().split(" ")))

    q = deque()
    visited = [[False for _ in range(chess_range)] for _ in range(chess_range)]
    
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    gaps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    while q:
        cur = q.popleft()
        if cur[0] == target_x and cur[1] == target_y:
            answers.append(cur[2])
            break
        for gap in gaps:
            if range_check((cur[0] + gap[0], cur[1] + gap[1]), chess_range) == False:
                continue
            if visited[cur[0] + gap[0]][cur[1] + gap[1]] == False:
                q.append((cur[0] + gap[0], cur[1] + gap[1], cur[2] + 1))
                visited[cur[0] + gap[0]][cur[1] + gap[1]] = True

for answer in answers:
    print(answer)