def f(x):
    return x-1
def findRoot(f,a,b,epsilon):
    while abs(b-a)>epsilon:
        m=(a+b)/2
        if f(m)*f(a)>0:
            a=m
        else:
            b=m
    print(m)
