import sys

totParams = len(sys.argv)

if (totParams < 2):
    print(" usage: python fibonacci.py n [--all]")
    exit()

n = int(sys.argv[1])

if (totParams > 2):
    all = sys.argv[2]

if (n <= 0):
    print("bah")
    exit()

if (n <= 2):
    if (all == "--all"):
        for i in range(0,n):
            print "fib(",i+1,") = 1"
    else:
        print(1)
    exit()


if (all == "--all"):
    print "fib( 1 ) = 1"
    print "fib( 2 ) = 1"
a = 1
b = 1
for i in range(2,n):
    next = a + b
    a = b
    b = next
    if (all == "--all"):
        print "fib(",i+1,") =",next

if (all != "--all"):
    print "fib(",n,") =",next