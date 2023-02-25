import sys

input = sys.stdin.readline

w, h = map(int, input().split())

front = []
front_reverse = []
side = []
side_reverse = []

for _ in range(w):
    front.append(int(input()))

for _ in range(h):
    side.append(int(input()))

front_height = max(front)
side_height = max(side)

def calc_min():
    total = 0
    for i in range(front_height):
        front_num = front.count(i+1)
        side_num = side.count(i+1)
        total += (i+1) * max(front_num, side_num)
    return total

def calc_max():
    front.sort()
    side.sort()

    total = 0
    for f in front:
        for s in side:
            total += min(f, s)
    return total

print(calc_min(), calc_max())