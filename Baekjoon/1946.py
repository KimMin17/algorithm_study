t = int(input())

def solve():
    n = int(input())

    app = []
    for _ in range(n):
        app.append(list(map(int, input().split())))
    
    app.sort(key=lambda x : (x[0], x[1]))

    answer = 0
    min_score = 10 ** 9
    
    for i in range(n):
        if app[i][1] < min_score:
            min_score = app[i][1]
            answer += 1
    return answer

answers = []
for _ in range(t):
    answers.append(solve())

for answer in answers:
    print(answer)