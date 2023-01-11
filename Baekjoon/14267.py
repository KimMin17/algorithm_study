n, m = tuple(map(int, input().split()))

praise = [0] * n
conn = list(map(int, input().split()))

for i in range(1, n):
    conn[i] -= 1

conn_list = [[i] for i in range(n)]

for cur in reversed(range(1, n)):
    parent = conn[cur]
    conn_list[parent] += conn_list[cur]

def solve(num, reward):
    for i in list(conn_list[num]):
        praise[i] += reward

for _ in range(m):
    num, reward = tuple(map(int, input().split()))
    solve(num - 1, reward)

print(*praise)