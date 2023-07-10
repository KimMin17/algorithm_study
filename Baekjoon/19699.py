from itertools import combinations

n, m = map(int, input().split())
cows = list(map(int, input().split()))

check_prime = [False] * 10000

def is_prime(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True

for i in range(2, 10000):
    if is_prime(i): check_prime[i] = True

combs = combinations(cows, m)

answers = set()
for comb in combs:
    total = sum(comb)
    if check_prime[total]: answers.add(total)

answers = list(answers)
answers.sort()

if answers:
    for answer in answers:
        print(answer, end = " ")
else:
    print(-1)