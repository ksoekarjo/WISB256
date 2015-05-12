def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return(ps)

import sys

import time
T1 = time.perf_counter()
primes(int(sys.argv[1]))
T2 = time.perf_counter()
fout=open(sys.argv[2],'w')
fout.write('\n'.join(str(i) for i in primes(int(sys.argv[1]))))
fout.close()
print('Found', len(primes(int(sys.argv[1]))), 'Prime numbers smaller than', sys.argv[1], 'in', T2 - T1, 'sec.')



