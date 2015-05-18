list=input().split()
a=float(list[0])
b=float(list[1])
c=list[2]
if c == '-':
    d = a-b
if c == '+':
    d = a+b
if c == '*':
    d = a*b
if c == '/':
    d = a/b
d = "{0:.3f}".format(d)
print(d)
