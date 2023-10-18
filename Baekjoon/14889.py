from itertools import combinations

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def get_score(team):
    score = 0
    for t1 in team:
        for t2 in team:
            if t1 != t2: score += graph[t1][t2]
    return score

combs = combinations(range(n), n//2)
done = []

def get_op(team):
    op = []
    for i in range(n):
        if i not in team: op.append(i)
    return op

answer = 10**9
for team1 in combs:
    team2 = get_op(team1)
    answer = min(answer, abs(get_score(team1) - get_score(team2)))
print(answer)