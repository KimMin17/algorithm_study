n, m = map(int, input().split())

t_set = set(list(map(int, input().split()))[1:])

p_list = []

for _ in range(m):
    p_list.append(set(list(map(int, input().split()))[1:]))

answer = 0

for _ in range(m):
    for p in p_list:
        if len(p.intersection(t_set)) != 0:
            t_set = t_set.union(p)

for p in p_list:
    if len(p.intersection(t_set)) == 0: answer += 1

print(answer)