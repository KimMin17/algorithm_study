def kmp():
    pass

text = input()
bomb = input()

while True:
    if len(text) == 0:
        text = "FRULA"
        break
    loc = text.find(bomb)
    if loc == -1: break
    text = text[:loc] + text[loc+len(bomb):]

print(text)