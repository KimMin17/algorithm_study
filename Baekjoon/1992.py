n = int(input())

img = []

for _ in range(n):
    img.append(list(map(int, list(input()))))

def solve(start_r, start_c, size):
    sum = 0
    result = "("
    for i in range(start_r, start_r+size):
        for j in range(start_c, start_c+size):
            sum += img[i][j]
    
    if sum == 0:
        return "0"
    elif sum == size**2:
        return "1"
    else:
        half_size = size // 2
        result += solve(start_r, start_c, half_size)
        result += solve(start_r, start_c + half_size, half_size)
        result += solve(start_r + half_size, start_c, half_size)
        result += solve(start_r + half_size, start_c + half_size, half_size)
        result += ")"
        return result

print(solve(0, 0, n))