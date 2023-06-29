n = int(input())

ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

answer = 0

for i in range(n):
    answer = max(answer, (i+1) * ropes[i])

print(answer)