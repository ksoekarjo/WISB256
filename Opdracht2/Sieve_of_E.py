import time
T1 = time.perf_counter()

N=int(input('Value for N?\n'))
numbers=list(range(N))
del numbers[0]
del numbers[0]
a=0
while a<len(numbers):
    i=a+1
    while i<len(numbers):
        if numbers[i]%numbers[a]==0:
            del numbers[i]
        i+=1
    a+=1
T2 = time.perf_counter()
fout=open('prime.dat','w')
fout.write("\n".join(str(i) for i in numbers))
fout.close()
print('Found', len(numbers), 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.')

