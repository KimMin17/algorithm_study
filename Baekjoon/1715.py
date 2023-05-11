'''
3
10
20
40
'''

from heapq import heappush, heappop

n = int(input())

cards = []

for _ in range(n):
    heappush(cards, int(input()))

if n == 1:
    print(0)
    exit()

answer = 0

while True:
    if len(cards) == 1: break
    card1 = heappop(cards)
    card2 = heappop(cards)

    new_cards = card1+card2
    answer += new_cards
    heappush(cards, new_cards)

print(answer)