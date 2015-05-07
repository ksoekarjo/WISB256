import sys
def drop_needle(L):
    import random
    import math
    # uniform in [0,1]
    x1 = random.random()
    # uniform in [0,2pi]
    a = random.vonmisesvariate(0,0)
    x2 = x1+L*math.sin(a)
    if x2>=1 or x2<=0:
        return True
    else:
        return False
N = int(sys.argv[1])
L = float(sys.argv[2])
if N ==0 or L ==0:
    print("Use: estimate_pi.py N L")
elif L>1 or L<0:
    print("L should be between 0 and 1")
else:
    i=1
    hits=0
    while i<= N:
        drop_needle(L)
        if drop_needle(L) == True:
            hits+=1
        i+=1
    pi=2*L/(hits/N)
    print(hits, "hits in", N, "tries")
    print("Pi =", pi)
