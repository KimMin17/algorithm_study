t = int(input())

answer = []

for _ in range(t):
    n = int(input())
    conn = [0] * (n+1)

    for _ in range(n-1):
        p, c = map(int, input().split())
        conn[c] = p

    cur1, cur2 = map(int, input().split())
    parents_1 = [cur1]
    parents_2 = [cur2]
    while True:
        p1, p2 = conn[cur1], conn[cur2]

        parents_1.append(p1)
        parents_2.append(p2)

        if p1 == p2:
            answer.append(p1)
            break
        if p2 in parents_1:
            answer.append(p2)
            break
        if p1 in parents_2:
            answer.append(p1)
            break
        
        cur1, cur2 = p1, p2

for item in answer:
    print(item)