import sys

input = sys.stdin.readline

w, h = map(int, input().split())

front = []
side = []

for _ in range(w):
    front.append(int(input()))

for _ in range(h):
    side.append(int(input()))

front.sort()
side.sort()

front_height = front[-1]
side_height = front[-1]

if front_height != side_height:
    print("-1")
    exit()

front_floor = [0] * front_height
side_floor = [0] * side_height

idx = 0
i = 0
while i < front_height and idx < len(front):
    if front[idx] > i:
        front_floor[i] = len(front) - idx
        i += 1
    else:
        idx += 1

idx = 0
i = 0
while i < side_height and idx < len(side):
    if side[idx] > i:
        side_floor[i] = len(side) - idx
        i += 1
    else:
        idx += 1

def calc_min():
    total = 0
    for i in range(len(front_floor)):
        front_num = front.count(i+1)
        side_num = side.count(i+1)
        total += (i+1) * max(front_num, side_num)
    return total

def calc_max():
    total = 0
    for i in range(front_height):
        total += front_floor[i] * side_floor[i]
    return total

print(calc_min(), calc_max())