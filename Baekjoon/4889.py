from collections import deque

def solve(txt):
    s = deque()
    answer = 0
    for c in txt:
        if c == "{":
            s.append(0)
        else:
            if len(s) == 0:
                answer += 1
                s.append(0)
            else:
                s.pop()
    return answer + len(s)//2

answers = []
while True:
    txt = input()
    if "-" in txt: break
    answers.append(solve(txt))

for i in range(len(answers)):
    print(str(i+1) + ".", answers[i])