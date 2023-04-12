'''
5 3
1 3 5 6 10
'''

n, k = map(int, input().split())

kids = list(map(int, input().split()))

diff = [0] * (n-1)

for i in range(n-1):
    diff[i] = (kids[i+1] - kids[i], i)

diff.sort(reverse=True)

splits = []
for i in range(k-1):
    splits.append(diff[i][1])

splits.sort()

answer = 0
start = 0
for s in splits:
    answer += kids[s] - kids[start]
    start = s + 1

answer += kids[n-1] - kids[start]
print(answer)