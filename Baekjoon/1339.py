n = int(input())

words = []

for i in range(n):
    words.append(input())

alph_set = []

for word in words:
    for alph in word:
        if alph not in alph_set: alph_set.append(alph)

sum_list = []

for alph in alph_set:
    alph_sum = 0
    for word in words:
        temp = list(word)
        for i in range(len(temp)):
            if temp[i] == alph: temp[i] = '1'
            else: temp[i] = '0'
        alph_sum += int("".join(temp))
    sum_list.append(alph_sum)

sum_list.sort(reverse=True)

answer = 0
num = 9

for item in sum_list:
    answer += (num * item)
    num -= 1

print(answer)