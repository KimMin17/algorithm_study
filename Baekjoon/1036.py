n = int(input())

nums = []

for _ in range(n):
    nums.append(input())

k = int(input())

def to_36(num_10):
    if int(num_10) < 10:
        return str(num_10)
    else:
        return str(chr(int(num_10) - 10 + 65))

def to_10(num_36):
    if num_36.isalpha():
        return ord(num_36) - 65 + 10
    else:
        return int(num_36)

def encode_to_36(num_10):
    result = ""
    while num_10 >= 36:
        result = to_36(num_10 % 36) + result
        num_10 //= 36
    result = to_36(num_10 % 36) + result
    return result

def decode_to_10(num_36):
    result = 0
    exp = 1
    for n in reversed(num_36):
        result += (to_10(n) * exp)
        exp *= 36
    return result

values = [0] * 36

def calc_value(num):
    exp = 1
    for n in reversed(num):
        values[to_10(n)] += exp
        exp *= 36

for num in nums:
    calc_value(num)

total_sum = 0
for _ in range(k):
    max_idx = -1
    max_diff = -1
    for i in range(35):
        if abs(35 * values[i] - i * values[i]) > max_diff:
            max_diff = abs(35 * values[i] - i * values[i])
            max_idx = i
    total_sum += 35 * values[max_idx]
    values[max_idx] = 0
    
for i in range(36):
    total_sum += (i * values[i])

print(encode_to_36(total_sum))