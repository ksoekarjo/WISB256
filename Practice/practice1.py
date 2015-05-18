n = int(input())
while n>0:
    line = input()
    if line.count(' ') <4:
        print(line, 'krAh!')
    else:
        print('Crackers!')
    n -= 1
