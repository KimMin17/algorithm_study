n = int(input())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort(reverse=True)
list_b.sort()

answer = 0
for i in range(n):
    answer += list_a[i] * list_b[i]

print(answer)