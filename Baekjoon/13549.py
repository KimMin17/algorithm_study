from collections import deque

n, k = map(int, input().split())

MAX_LEN = 200000

visited = [False] * MAX_LEN

def range_check(loc):
    if loc < 0 or loc >= MAX_LEN: return False
    else: return True

q = deque()

q.append((0, n))
visited[n] = True

while q:
    cur_time, cur_loc = q.popleft()
    
    if cur_loc == k:
        print(cur_time)
        exit()

    next_loc = cur_loc*2
    next_time = cur_time

    if range_check(next_loc):
        if not visited[next_loc]:
            if next_loc == k:
                print(next_time)
                exit()
            q.appendleft((next_time, next_loc))
            visited[next_loc] = True

    next_loc = cur_loc+1
    next_time = cur_time+1

    if range_check(next_loc):
        if not visited[next_loc]:
            if next_loc == k:
                print(next_time)
                exit()
            q.append((next_time, next_loc))
            visited[next_loc] = True
    
    next_loc = cur_loc-1
    next_time = cur_time+1

    if range_check(next_loc):
        if not visited[next_loc]:
            if next_loc == k:
                print(next_time)
                exit()
            q.append((next_time, next_loc))
            visited[next_loc] = True