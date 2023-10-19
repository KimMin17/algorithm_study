t = int(input())

answers = []

def solve(n, l):
    l.sort()
    new_l = []

    for i in range(0, n, 2):
        new_l.append(l[i])
    for i in reversed(range(1, n, 2)):
        new_l.append(l[i])

    max_diff = -1

    for i in range(n):
        max_diff = max(max_diff, abs(new_l[i] - new_l[(i+1)%n]))

    return max_diff

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    answers.append(solve(n, l))

for answer in answers:
    print(answer)