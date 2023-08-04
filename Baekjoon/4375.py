answers = []

def solve(div_num, answers):
    num = 1
    exp = 10
    count = 1

    while True:
        if num % div_num == 0:
            answers.append(count)
            break
        else:
            num += exp
            exp *= 10
            count += 1

while True:
    try:
        solve(int(input()), answers)
    except:
        break

for answer in answers:
    print(answer)