n = int(input())
answer = 0

row = [0] * n

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]): return False
    return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return

    for i in range(n):
        row[x] = i
        if check(x):
            n_queens(x+1)

n_queens(0)
print(answer)