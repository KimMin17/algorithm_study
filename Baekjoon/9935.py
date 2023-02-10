from collections import deque

text = input()
bomb = input()

bomb_len = len(bomb)
bomb_last_alph = bomb[-1]

stack = deque()

for alph in text:
    stack.append(alph)
    if alph == bomb_last_alph:
        check = ""
        if len(stack) >= bomb_len:
            for _ in range(bomb_len):
                check = stack.pop() + check
            if check != bomb:
                for item in check: stack.append(item)

if len(stack) == 0:
    print("FRULA")
else:
    while stack:
        print(stack.popleft(), end = "")