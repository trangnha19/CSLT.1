x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch=='+':
    kq=x+y
    print(x,ch,y,'=',round(kq,1),sep='')
elif ch=='-':
    kq=x-y
    print(x,ch,y,'=',round(kq,1),sep='')
elif ch=='*':
    kq=x*y
    print(x,ch,y,'=',round(kq,1),sep='')
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        kq=x/y
        print(x,ch,y,'=',round(kq,1),sep='')
else:
    print('Khong hop le')

    
    