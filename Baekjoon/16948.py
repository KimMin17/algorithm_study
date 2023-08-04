from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

visited = [[False] * n for _ in range(n)]

def check_range(r, c):
    if 0 <= r < n and 0 <= c < n: return True
    else: return False

q = deque()

gaps = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

q.append((r1, c1, 0))
visited[r1][c1] = True

while q:
    cur_r, cur_c, step = q.popleft()

    for gap in gaps:
        next_r, next_c = cur_r + gap[0], cur_c + gap[1]
        if check_range(next_r, next_c):
            if not visited[next_r][next_c]:
                if next_r == r2 and next_c == c2:
                    print(step+1)
                    exit()
                q.append((next_r, next_c, step+1))
                visited[next_r][next_c] = True

print(-1)