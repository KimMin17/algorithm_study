'''
7
9 9 4 1 4 9 9

7
4 4 9 1 9 4 4

3
2 5 4
'''
import sys
input = sys.stdin.readline

n = int(input())

honey = list(map(int, input().split()))

left_max = 0
right_max = 0
center_max = 0

temp = [0] * n
temp[0] = honey[0]
for i in range(1, n):
    temp[i] = temp[i-1] + honey[i]

for i in range(1, n-1):
    left_max = max(left_max, temp[i-1] + temp[n-1] - honey[i] - honey[n-1])
    right_max = max(right_max, temp[n-1] - honey[0] - honey[i] + temp[n-1] - temp[i])

center_max = temp[n-1] - honey[0] - honey[n-1] + max(honey)

print(max(left_max, right_max, center_max))