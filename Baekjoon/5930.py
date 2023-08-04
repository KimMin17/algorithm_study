from collections import deque

n = int(input())

notes = deque()
for _ in range(n): notes.append(int(input()))

c = int(input())

example = []
for _ in range(c): example.append(int(input()))

example.sort()
min_val = example[0]
for i in range(c): example[i] -= min_val

dq = deque()
for _ in range(c):
    dq.append(notes.popleft())

def check(target, example, c):
    target.sort()
    min_val = target[0]
    for i in range(c): target[i] -= min_val

    for i in range(c):
        if target[i] != example[i]: return False
    return True

answers = []
idx = 1
while True:
    if check(list(dq), example, c): answers.append(idx)
    if len(notes) == 0: break
    dq.popleft()
    dq.append(notes.popleft())
    idx += 1

print(len(answers))
for answer in answers:
    print(answer)