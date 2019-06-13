import sys
import time

totParams = len(sys.argv)

if (totParams < 2):
    print(" usage: python recaman.py n")
    exit()

n = int(sys.argv[1])

used = set()

next_goal = 1
i = 0
pos = 0
used.add(0)
print("0 -> 0")

while 1:
    i = i + 1
    if (pos - i) < 0 or (pos - i) in used:
        pos = pos + i
    else:
        pos = pos - i
    
    used.add(pos)
    
    print i,"->",pos
    
    if (pos == next_goal):
        for j in range(next_goal,n+1):
            if j not in used:
                next_goal = j
                break

    if (next_goal == n):
        break