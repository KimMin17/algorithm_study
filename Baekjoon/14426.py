n, m = map(int, input().split())

words = []
prefixes = []

for _ in range(n):
    words.append(input())

for _ in range(m):
    prefixes.append(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def move_next(self, data):
        for child in self.children:
            if child.data == data:
                return child
        new_child = Node(data)
        self.children.append(new_child)
        return new_child  

root = Node(None)

def make_tree(word):
    cur = root
    for c in word:
        cur = cur.move_next(c)

for word in words:
    make_tree(word)


def solve(prefix):
    cur = root
    for c in prefix:
        found = False
        for child in cur.children:
            if child.data == c:
                cur = child
                found = True
                break
        if not found: return 0
    return 1

answer = 0
for prefix in prefixes:
    answer += solve(prefix)
print(answer)