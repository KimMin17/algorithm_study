n, m = map(int, input().split())

well = list(map(int, input().split()))
well.insert(0, 0)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (n+1)
answer = 0

def dfs(node, before):
    global answer

    visited[node] = True
    cur_well = 0
    for c in graph[node]:
        if visited[c]: continue
        dfs(c, node)
        cur_well = max(cur_well, well[c])
    
    answer += cur_well
    well[node] -= cur_well
    for c in graph[node]:
        well[c] -= cur_well

dfs(1, -1)
if well[1] > 0: answer += well[1]
print(answer)