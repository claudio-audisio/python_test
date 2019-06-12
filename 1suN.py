import sys

totParams = len(sys.argv)

if (totParams != 2):
    print(" usage: python 1suN.py n")
    exit()

n = int(sys.argv[1])

tot = float(0)

for i in range(0,n):
    tot = tot + 1/float(i+1)
    
print(tot)
