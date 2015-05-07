import sys
import random
import math
if len(sys.argv)==4:
    random.seed(int(sys.argv[3]))
def drop_needle(L):
    # uniform in [0,1]
    x1 = random.random()
    # uniform in [0,2pi]
    a = random.vonmisesvariate(0,0)
    x2 = x1+L*math.sin(a)
    if x2>=1 or x2<=0:
        return True
    else:
        return False
if len(sys.argv)<=2:
    print("Use: estimate_pi.py N L")
else:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
    if L<=0:
        print("L should be greater than 0")
    else:
        i=1
        hits=0
        while i<= N:
            drop_needle(L)
            if drop_needle(L) == True:
                hits+=1
            i+=1
        if L<=1:
            pi=2*L/(hits/N)
        else:
            pi=(2*L-2*(math.sqrt(L**2-1)+math.asin(1/L)))/(hits/N-1)
        print(hits, "hits in", N, "tries")
        print("Pi =", pi)
