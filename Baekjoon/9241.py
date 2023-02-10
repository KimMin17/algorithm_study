from collections import deque

dna = input()
changed = input()

dna_deque = deque(dna)
changed_deque = deque(changed)

if dna == changed:
    print("0")
    exit()

while True:
    if len(dna_deque) == 0:
        print(len(changed_deque))
        exit()

    if len(changed_deque) == 0: break

    done = True
    if dna_deque[0] == changed_deque[0]:
        dna_deque.popleft()
        changed_deque.popleft()
        done = False
    
    if len(dna_deque) == 0:
        print(len(changed_deque))
        exit()

    if len(changed_deque) == 0: break

    if dna_deque[-1] == changed_deque[-1]:
        dna_deque.pop()
        changed_deque.pop()
        done = False
    
    if done: break

print(len(changed_deque))