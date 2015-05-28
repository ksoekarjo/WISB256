def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if abs(b-a)<epsilon:
        return m
    else:
        if f(m)*f(a)>0:
            return findRoot(f,m,b,epsilon)
        else:
            return findRoot(f,a,m,epsilon)

