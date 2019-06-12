import sys
import time

if (len(sys.argv) != 2):
    print(" usage: factorial_vs_exp <base_exp>")
    quit()


count = 1
fact = 1
base_exp = int(sys.argv[1])
tot_exp = base_exp

while fact < tot_exp:
    count = count + 1
    fact =  fact * count
    tot_exp = tot_exp * base_exp
    #print(count,"! -> ", fact)
    #print(base_exp,"^",count," -> ", tot_exp)    
    #time.sleep(1)

print("\nn ! factorial is major then", base_exp, "^ n for n >=", count, "\n")
print(count,"! -> ", fact)
print(base_exp,"^",count," -> ", tot_exp)
