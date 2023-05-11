'''
4
4 4
5 2
11 5
15 10
25 10

5
3 5
6 4
7 8
11 3
18 5
20 5
'''
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())

gas_station = []

for _ in range(n):
    dist, gas = map(int, input().split())
    heappush(gas_station, (dist, gas))

town_dist, start_gas = map(int, input().split())

cur_gas = start_gas
count = 0

target_list = []

while True:
    if cur_gas >= town_dist: break
    while gas_station:
        dist, gas = heappop(gas_station)
        if cur_gas >= dist:
            gas *= -1
            heappush(target_list, (gas, dist))
        else:
            heappush((gas_station), (dist, gas))
            break
        
    if len(target_list) > 0:
        gas, dist = heappop(target_list)
        gas *= -1
        cur_gas += gas
        count += 1
    else:
        print(-1)
        exit()

print(count)