n = int(input())

information = []

for _ in range(n):
    information.append(input().split()[1:])

class node:
    def __init__(self, name):
        self.name = name
        self.child_list = {}

root = node("root")

def make_tree(info):
    cur_node = root
    for room in info:
        if not room in cur_node.child_list:
            cur_node.child_list[room] = node(room)
        cur_node = cur_node.child_list[room]

for info in information:
    make_tree(info)

def print_tree(node, depth):
    for _ in range(depth):
        print("--", end = "")
    print(node.name)
    for key, value in sorted(node.child_list.items()):
        print_tree(value, depth+1)

for key, value in sorted(root.child_list.items()):
    print_tree(value, 0)