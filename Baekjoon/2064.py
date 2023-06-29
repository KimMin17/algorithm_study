n = int(input())

ip_list = []

def conv_ip(ip):
    result = 0
    exp = 1

    for i in reversed(range(4)):
        result += (int(ip[i]) * exp)
        exp <<= 8

    return result

for _ in range(n):
    ip_list.append(conv_ip(input().split(".")))

full_mask = (1 << 32) - 1
mask = full_mask

def get_mask(mask):
    global full_mask
    while mask:
        network = ip_list[0] & mask
        flag = True
        for i in range(1, n):
            if network != (ip_list[i] & mask):
                mask = (mask << 1) & full_mask
                flag = False
                break
        if flag: return mask
    return 0

mask = get_mask(mask)

def conv_bin(b):
    result = []
    for _ in range(4):
        result.insert(0, b % 256)
        b //= 256
    return result

print(".".join(map(str, conv_bin(mask & ip_list[0]))))
print(".".join(map(str, conv_bin(mask))))