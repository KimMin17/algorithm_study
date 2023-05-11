'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
'''
n = int(input())

wires = []

for _ in range(n):
    wires.append(tuple(map(int, input().split())))

wires.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))