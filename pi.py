import sys
import math

totParams = len(sys.argv)

if (totParams != 2):
    print(" usage: python pi.py n")
    exit()

n = int(sys.argv[1])

tot = float(1)

# Prodotto di Wallis per il calcolo di pigreco
for i in range(1,n):
    tot = tot * ( (2.0*2.0*i*i) / ( ((2.0*i) - 1) * ((2.0*i) + 1) ) )
    
print(tot*2.0)