from itertools import combinations

tests = []
while True:
    test = input()
    if test == '0': break
    tests.append(test)

for test in tests:
    test = list(map(int, test.split()))
    combs = combinations(test[1:], 6)

    for comb in combs:
        print(*comb)
    print()