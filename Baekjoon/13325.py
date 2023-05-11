'''
2
2 2 2 1 1 3
'''

k = int(input())

edges = list(map(int, input().split()))
edges.insert(0, 0)

dp = [0] * (2**(k+1)-1)
weight = [0] * (2**k)

def find_parent(node):
    return (node-1) // 2

def find_child(node):
    return (node*2+1, node*2+2)

for i in range(1, 2**(k+1)-1):
    dp[i] = dp[find_parent(i)] + edges[i]

for i in range(1, 2**k+1):
    weight[-i] = dp[-i]

goal = max(weight)
answer = sum(edges)

def get_weight(start, end):
    global answer
    if start == end: answer += goal - weight[start]
    else:
        add_val = goal - max(weight[start:end+1])
        answer += add_val
        for i in range(start, end+1): weight[i] += add_val
        get_weight(start, (start+end) // 2)
        get_weight((start+end) // 2 + 1, end)

get_weight(0, (2**k-1)//2)
get_weight((2**k-1)//2+1, (2**k-1))
print(answer)