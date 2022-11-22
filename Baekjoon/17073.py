import sys
from collections import deque

input = sys.stdin.readline

n, w = tuple(map(int, input().split()))

node_list = [[] for _ in range(n)]

for _ in range(n-1):
    p, c = tuple(map(int, input().split()))
    node_list[p-1].append(c-1)

pi_dict = {0: 10000}

