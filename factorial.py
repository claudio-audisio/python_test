import sys
import time

if (len(sys.argv) != 2):
    print(" usage: factorial <n>")
    quit()

fact = 1
n = int(sys.argv[1])

for i in range(2, n+1):
    fact = fact * i
    print(i,"! -> ", fact)
    #time.sleep(0.1)

#print(n,"! -> ", fact)
