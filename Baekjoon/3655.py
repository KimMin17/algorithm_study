t = int(input())

answers = []

def solve():
    n = int(input())
    groups = list(input())

    last_idx = {}

    for i in reversed(range(n)):
        if groups[i] not in last_idx: last_idx[groups[i]] = i+1

    not_saved_time = 0

    for i in range(n):
        groups[i] = last_idx[groups[i]]
    
    not_saved_time = sum(groups)

    saved_time = 0
    groups.sort()

    new_last_idx = {}
    for i in reversed(range(n)):
        if groups[i] not in new_last_idx: new_last_idx[groups[i]] = i+1
    for i in range(n):
        saved_time += new_last_idx[groups[i]]

    return (not_saved_time - saved_time) * 5

for _ in range(t):
    answers.append(solve())

for answer in answers:
    print(answer)