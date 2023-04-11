a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b and a>c:
    SLN=a
elif b>c:
    SLN=b
else:
    SLN=c
print('SLN=',SLN,sep='')
if a<b and a<c:
    SNN=a
elif b<c:
    SNN=b
else:
    SNN=c
print('SNN=',SNN,sep='')
