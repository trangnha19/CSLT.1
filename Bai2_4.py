a=float(input('Do dai canh thu nhat:'))
b=float(input('Do dai canh thu hai:'))
c=float(input('Do dai canh thu ba:'))
s=(a+b+c)/2
import math
print('Dien tich=',math.sqrt(s*(s-a)*(s-b)*(s-c)))