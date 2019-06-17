import sys
import math

totParams = len(sys.argv)

if (totParams != 2):
    print(" usage: python 1onNpowX.py x")
    exit()

esp = float(sys.argv[1])

tot = float(0)

i = 1

while True:
    tot = tot + 1.0/pow(i, esp)

    if (i % 1000000 == 0):
        print tot," on",i/1000000,"M)"

    i = i + 1
