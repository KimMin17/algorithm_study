n = int(input())

arr = list(map(int, input().split()))
arr.sort()

sum_val = 10000000000000

answers = (0, 0, 0)

for i in range(n-2):
    l_idx = i+1
    r_idx = n-1
    
    while l_idx < r_idx:
        val = arr[i]+arr[l_idx]+arr[r_idx]
        if abs(val) < abs(sum_val):
            sum_val = val
            answers = arr[i], arr[l_idx], arr[r_idx]
        if val == 0:
            print(*answers)
            exit()
        elif val > 0: r_idx -= 1
        else: l_idx += 1

print(*answers)