#A005132
#Recaman's sequence (or Recaman's sequence): a(0) = 0; for n > 0, a(n) = a(n-1) - n if positive and not already in the sequence, otherwise a(n) = a(n-1) + n.

import sys
import time

totParams = len(sys.argv)

if (totParams < 2):
    print(" usage: python recaman.py n")
    exit()

n = int(sys.argv[1])

recamam = dict()

next_goal = 1
prev_goal = 0
i = 0
pos = 0
recamam[0] = 0

alldone = False

while alldone == False:
    i = i + 1
    if (pos - i) < 0 or (pos - i) in recamam:
        pos = pos + i
    else:
        pos = pos - i
    
    recamam[pos] = i
    
    if (i % 10000000 == 0):
        print("passed",int(i/1000000),"million(s) iterations searching", next_goal)
    
    if (pos == next_goal):

        print("rec(",next_goal,") ->",recamam[next_goal]) 
        #for j in range (prev_goal + 1, next_goal + 1):
            #print("rec(",j,") ->",recamam[j])

        prev_goal = next_goal

        while 1:
            next_goal = next_goal + 1

            if (next_goal > n):
                alldone = True
                break

            if next_goal not in recamam:
                #print("next goal:", next_goal)
                break

            print("rec(",next_goal,") ->",recamam[next_goal])

print("with", i, "iterations")