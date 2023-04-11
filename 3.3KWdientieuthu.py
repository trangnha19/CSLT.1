KW=int(input('Tieu thu='))
if 1<=KW and KW<=100:
    Tien=KW*550
elif 101<=KW and KW<=150:
    Tien=(KW-100)*750+100*550
elif 151<=KW and KW<=200:
    Tien=(KW-150)*950+100*550+50*750
else:
    Tien=(KW-200)*1350+100*550+50*750+50*950
VAT=10/100
print('Phai tra=',(Tien+Tien*VAT), sep='')