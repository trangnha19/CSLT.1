M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S<=100:
    Gia=M1
    print('Phai tra=',S*M1,sep='')
elif S>100 and S<=150:
    Gia=M2
    print('Phai tra=',(S-100)*M2+S*M1,sep='')
else:
    Gia=M3
    print('Phai tra=',(S-150)*M3+50*M2+100*M1,sep='')