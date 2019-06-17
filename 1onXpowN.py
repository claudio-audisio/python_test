import sys
import math
import time

totParams = len(sys.argv)

if (totParams != 2):
    print(" usage: python 1onXpowN.py x")
    exit()

base = float(sys.argv[1])

tot = float(1)

i = 1

while True:
    prev_tot = tot
    tot = tot + 1.0/pow(base, i)

    print tot," on",i

    if (prev_tot == tot):
        break

    i = i + 1

    #time.sleep(0.1)
