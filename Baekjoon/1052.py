n, k = map(int, input().split())

count = 0
while True:
    binary = bin(n)
    b_count = 0
    for b in binary:
        if b == '1': b_count += 1
    
    if b_count <= k: break
    n += 1
    count += 1

print(count)