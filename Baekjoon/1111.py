'''
4
1 4 13 40
'''

n = int(input())

numbers = list(map(int, input().split()))

if n < 2:
    print("A")
    exit()

if n == 2:
    if numbers[0] == numbers[1]: print(numbers[0])
    else: print("A")
    exit()

def escape():
    print("B")
    exit()

def solve_equation(n1, n2, n3):
    if n1 == n2: a = 0
    else: a = (n3-n2) / (n2-n1)
    b = n2 - (a * n1)

    if int(a) != a or int(b) != b:
        escape()
    
    return (int(a), int(b))

a, b = solve_equation(numbers[0], numbers[1], numbers[2])

next_num = a * numbers[0] + b
for i in range(1, n):
    if next_num == numbers[i]:
        next_num = a * numbers[i] + b
    else:
        escape()

print(int(next_num))