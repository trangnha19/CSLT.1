toan=float(input(''))
ly=float(input(''))
hoa=float(input(''))
ĐTB=(ly*3+toan*2+hoa)/6
if ĐTB<3:
    print('Kém')
elif 3<=ĐTB<5:
    print('Yếu')
elif 5<=ĐTB<6:
    print('Trung bình')
elif 6<=ĐTB<7:
    print('Trung bình Khá')
elif 7<=ĐTB<8:
    print('Khá')
elif 8<=ĐTB<9:
    print('Giỏi')
elif 9<=ĐTB and ĐTB<10:
    print('Xuất sắc')


