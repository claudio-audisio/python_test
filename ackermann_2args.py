#The Ackermann function is the simplest example of a well-defined total function which is computable but not primitive recursive,
#providing a counterexample to the belief in the early 1900s that every computable function was also primitive recursive (Dötzel 1991).
#It grows faster than an exponential function, or even a multiple exponential function.

#Ackermann's function (2 arguments)

import sys
import time

totParams = len(sys.argv)

class CallCounter:
    counter = 0
    def __init__(self):
        self.counter = 0
    def call(self):
        self.counter = self.counter + 1 
        if (self.counter % 10000000 == 0):
            print("reached ",self.counter," calls")
    def reset(self):
        self.counter = 0
    def get(self):
        return self.counter

class AckermannDict:
    ack_dict = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}} 
    def get(self, m, n):
        if (m in self.ack_dict) and (n in self.ack_dict[m]):
            return self.ack_dict[m][n]
        return 0
    def set(self, m, n, res):
        self.ack_dict[m][n] = res

ack_dict = AckermannDict()
counter = CallCounter()

def Ackermann(m,n):
    counter.call()
    if (m == 0):
        return n+1
    else:
        res = 0
        if (n == 0):
            res = ack_dict.get(m-1, 1)
            if (res > 0):
                return res
            return Ackermann(m-1, 1)
        else:
            res = ack_dict.get(m, n-1)
            if (res > 0):
                res2 = ack_dict.get(m-1, res)
                if (res2 > 0):
                    return res2
                return Ackermann(m-1, res)
            return Ackermann(m-1, Ackermann(m, n-1))

def GetMaxN(m):
    if (m == 0): return 1049002
    if (m == 1): return 1049000
    if (m == 2): return 524300
    if (m == 3): return 20
    return 10

m = 0
n = 0
counter.reset()
sys.setrecursionlimit(100000)
print("run with ", sys.getrecursionlimit(), " recursion limit")
prev = 0

while True:
    n = 0
    max_n = GetMaxN(m)
    while n <= max_n:
        if (m == 3) and (n == 7):
            stop = 1
        res = Ackermann(m,n)
        ack_dict.set(m, n, res)
        if (n > 0):
            print("A(",m,",",n,") --> ",res," with ",counter.get()," calls (diff ",counter.get() - prev," - growth ratio ",counter.get() / prev,")")
        else:
            print("A(",m,",",n,") --> ",res," with ",counter.get()," calls (diff ",counter.get() - prev,")")
        prev = counter.get()

        if (prev > 1):
            time.sleep(10)

        counter.reset()
        n = n + 1
    m = m + 1