n= int(input())
s=list(input())
s= [int(i) for i in s]
klappers=s[0]
a=1
while a<len(s):
    if s[a]>0:
        while a>klappers:
            klappers +=1
        klappers += s[a]
    a += 1
extra = klappers - sum(s)
print(extra)
