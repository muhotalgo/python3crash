# 26. 사용자가 연봉과 결혼 여부를 입력하면 다음의 세금율에 의해 납부해야할 세금을 계산하는 프로그램을 작성하세요 (Tax)

isMarried = input('결혼여부는? (1:미혼, 2:기혼)')
sal = int(input('연봉은? '))

if isMarried == '1':
    if sal >= 3000: tax = sal * 0.25
    else: tax = sal * 0.1
else:
    if sal >= 6000: tax = sal * 0.35
    else: tax = sal * 0.15

print(f'{isMarried} {sal} {tax}')


# 33. 임의의 숫자 6자리를 입력하면 신용카드의 종류와 은행정보를 출력하는 프로그램을 작성해보세요.  (CardCheck)

# 35(JCB카드)
# 356317 - NH농협카드, 356901 - 신한카드, 356912 - KB국민카드
# 4(비자카드)
# 404825 – 비씨카드, 438676 – 신한카드, 457973 – 국민은행
# 5(마스타카드, Maestro)
# 515594 – 신한카드, 524353 - 외환카드, 540926 – 국민은행

cardnum = input('카드번호는? ')

if cardnum == '356317': cardname = 'JCB카드 NH농협카드'
elif  cardnum == '356901': cardname = 'JCB카드 신한카드'
elif  cardnum == '356912': cardname = 'JCB카드 KB국민카드'
elif  cardnum == '404825': cardname = '비자카드 비씨카드'
elif  cardnum == '438676': cardname = '비자카드 신한카드'
elif  cardnum == '457973': cardname = '비자카드 국민은행'
elif  cardnum == '515594': cardname = '마스타카드 신한카드'
elif  cardnum == '524353': cardname = '마스타카드 외환카드'
elif  cardnum == '540926': cardname = '마스타카드 국민은행'
else: cardname = '없는 카드'

print(f'{cardnum} {cardname}')

# 35. 시간때를 의미하는 영어단어를 변수 daytime으로 입력받으면,
# 그에 따른 의미를 출력하는 프로그램을 작성하라 (CheckDayTime)
#
#
# morning hours                 아침시간 (7-12)
# midday / noon                 점심시간 (12-1)
# afternoon hours               오후 (1-6)
# evening hours                 저녁시간 (6-9)
# night hours                   밤시간 (9-12)
# midnight                      자정시간 (12)
# early morning hours           새벽시간 (12-5)
# small hours                   새벽 (1-3)
# dawn / daybreak               해뜰력 (5-7)

daytime = input('시간대는? ')

if daytime == 'morning hours': engdt = '아침시간 (7-12)'
elif daytime == 'midday' or daytime == 'noon': engdt = '점심시간(12-1)'
elif daytime == 'afternoon hours': engdt = '오후 (1-6)'
elif daytime == 'evening hours': engdt = '저녁시간 (6-9)'
elif daytime == 'night hours': engdt = '밤시간 (9-12)'
elif daytime == 'midnight': engdt = '자정시간 (12)'
elif daytime == 'early morning hours': engdt = '새벽시간 (12-5)'
elif daytime == 'small hours': engdt = '새벽 (1-3)'
elif daytime == 'dawn' or daytime == 'daybreak': engdt = '해뜰력 (5-7)'
else: engdt = '없음'

print(f'{daytime} {engdt}')

# 48. 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라 가정할 때, 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을
# 아래 그림을 참고하여 작성하여라. (ComputeInvestment)

account = 25000
interest = 1.06
limit = account * 2


for i in range(1, 20+1):
    account = account * interest
    print(f'{i} 년차 통장잔액 {account:,.0f}')


# 51. 아래의 그림처럼 결과를 출력하는 프로그램을 작성하여라. (BigGugudan)

print('                 Multiplication Table')
print('             1   2   3   4   5   6   7   8   9')
print('--------------------------------------------------')
print('1   |        1   2   3   4   5   6   7   8   9')
print('2   |        2   4   6   8  10  12  14  16  18')
print('3   |        3   6   9  12  15  18  21  24  27')
print('4   |        4   8  12  16  20  24  28  32  36')
print('5   |        5  10  15  20  25  30  35  40  45')
print('6   |        6  12  18  24  30  36  42  48  54')
print('7   |        7  14  21  28  35  42  49  56  63')
print('8   |        8  16  24  32  40  48  56  64  72')
print('9   |        9  18  27  36  45  54  63  72  81')

print('                 Multiplication Table')
print('             1   2   3   4   5   6   7   8   9')
print('--------------------------------------------------')
for i in range(1, 9+1):
    print(f'{i}   |       ', end='')
    for j in range(1, 9+1):
        print(f'{i*j:2d}  ', end='')
    print()







for i in range (1, 9+1):
    print(i)


