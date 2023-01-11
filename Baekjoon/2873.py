def find_loc_not_visit(board, r, c):
    min_val = 1234
    loc_i, loc_j = 0, 0
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 1 and board[i][j] < min_val:
                min_val = board[i][j]
                loc_i, loc_j = i, j
    return loc_i, loc_j

r, c = tuple(map(int, input().split()))

board = []

for _ in range(r):
    board.append(list(map(int, input().split())))

if c % 2 != 0:
    direction = 1
    for i in range(c):
        for j in range(r - 1):
            if direction == 1:
                print("D", end="")
            elif direction == -1:
                print("U", end="")
        direction *= -1
        if i != c - 1: print("R", end="")
elif r % 2 != 0:
    direction = 1
    for i in range(r):
        for j in range(c - 1):
            if direction == 1:
                print("R", end="")
            elif direction == -1:
                print("L", end="")
        direction *= -1
        if i != r - 1: print("D", end="")
else:
    loc_i, loc_j = find_loc_not_visit(board, r, c)
    caution_col = loc_j
    if caution_col % 2 == 1: caution_col -= 1

    direction = 1
    for i in range(caution_col):
        for j in range(r - 1):
            if direction == 1:
                print("D", end="")
            elif direction == -1:
                print("U", end="")
        direction *= -1
        if i != c - 1: print("R", end="")

    direction = 1
    for i in range(r - 1):
        if i == loc_i:
            print("D", end="")
        else:
            if direction == 1: print("R", end="")
            elif direction == -1: print("L", end="")
            if i != r - 1: print("D", end="")
            direction *= -1
    if direction == 1: print("R", end="")
    if caution_col != c - 2: print("R", end="")

    direction = -1
    for i in range(caution_col + 2, c):
        for j in range(r - 1):
            if direction == 1:
                print("D", end="")
            elif direction == -1:
                print("U", end="")
        direction *= -1
        if i != c - 1: print("R", end="")