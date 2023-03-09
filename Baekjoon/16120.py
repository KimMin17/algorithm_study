from collections import deque

txt = input()

s = deque()

for t in txt:
    s.append(t)
    if len(s) >= 4:
        if s[-4] + s[-3] + s[-2] + s[-1] == "PPAP":
            for _ in range(3): s.pop()

if "".join(list(s)) == "P": print("PPAP")
else: print("NP")