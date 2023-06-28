from heapq import heappop, heappush

n, m = map(int, input().split())

books = list(map(int, input().split()))

pos_loc = []
neg_loc = []

for book in books:
    if book >= 0: heappush(pos_loc, -book)
    else: heappush(neg_loc, book)

answer = 0

while pos_loc:
    max_book = heappop(pos_loc)
    max_book *= -2
    answer += max_book
    for _ in range(m-1):
        if len(pos_loc) == 0: break
        heappop(pos_loc)


while neg_loc:
    max_book = heappop(neg_loc)
    max_book *= -2
    answer += max_book
    for _ in range(m-1):
        if len(neg_loc) == 0: break
        heappop(neg_loc)

abs_max = 0
for book in books:
    abs_max = max(abs_max, abs(book))
answer -= abs_max
print(answer)