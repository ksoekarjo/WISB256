row1=list(input())
row2=list(input())
row3=list(input())
if row1[0]==row1[1]==row1[2] != '0':
    if row1[0]=='1':
        print('Player 1 wins')
    if row1[0]=='2':
        print('Player 2 wins')
elif row2[0]==row2[1]==row2[2] != '0':
    if row2[0]=='1':
        print('Player 1 wins')
    if row2[0]=='2':
        print('Player 2 wins')
elif row3[0]==row3[1]==row3[2] != '0':
    if row3[0]=='1':
        print('Player 1 wins')
    if row3[0]=='2':
        print('Player 2 wins')
elif row1[0]==row2[0]==row3[0] != '0':
    if row1[0]=='1':
        print('Player 1 wins')
    if row1[0]=='2':
        print('Player 2 wins')
elif row1[1]==row2[1]==row3[1] != '0':
    if row1[1]=='1':
        print('Player 1 wins')
    if row1[1]=='2':
        print('Player 2 wins')
elif row1[2]==row2[2]==row3[2] != '0':
    if row1[2]=='1':
        print('Player 1 wins')
    if row1[2]=='2':
        print('Player 2 wins')
elif row1[0]==row2[1]==row3[2] != '0':
    if row1[0]=='1':
        print('Player 1 wins')
    if row1[0]=='2':
        print('Player 2 wins')
elif row1[2]==row2[1]==row3[0] != '0':
    if row1[2]=='1':
        print('Player 1 wins')
    if row1[2]=='2':
        print('Player 2 wins')    
else:
    print('No winner')
