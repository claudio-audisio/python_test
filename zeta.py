import sys
import time
import math

totParams = len(sys.argv)

if (totParams < 2):
    print(" usage: python zeta.py n")
    exit()

n = float(sys.argv[1])

res = 0.0
i = 1

while True:
    res = res + (1.0 / math.pow(i, n))

    if (i % 1000000 == 0):
        print res," on",i/1000000,"M)"

    i = i + 1
