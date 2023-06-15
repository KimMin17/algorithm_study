import sys

sys.setrecursionlimit(200001)

n = int(input())

info = list(map(int, input().split()))

conn = [[] for _ in range(n)]

conn_info = list(map(int, input().split()))

for i in range(n-1):
    conn[conn_info[i]-1].append(i+1)

dp = [[0, 0] for _ in range(n)]
attend = [False] * n

N = 0
Y = 1

def dfs(node, flag):
    if dp[node][flag] != 0: return dp[node][flag]

    if flag == Y:
        for next_node in conn[node]:
            dp[node][flag] += dfs(next_node, N)
        attend[node] = True
        dp[node][flag] += info[node]
    else:
        for next_node in conn[node]:
            Y_result = dfs(next_node, Y)
            N_result = dfs(next_node, N)
            if Y_result > N_result:
                dp[node][flag] += Y_result
                attend[next_node] = True
            else:
                dp[node][flag] += N_result
                attend[next_node] = False
    return dp[node][flag]

attend_list = []
def trace(node, flag):
    if flag == Y: attend_list.append(node+1)

    for next_node in conn[node]:
        if flag == Y: trace(next_node, N)
        else:
            if attend[next_node]: trace(next_node, Y)
            else: trace(next_node, N)
        

Y_MAX = dfs(0, Y)
N_MAX = dfs(0, N)

print(Y_MAX, N_MAX)
trace(0, Y)
print(*sorted(attend_list), -1)
attend_list.clear()
trace(0, N)
print(*sorted(attend_list), -1)