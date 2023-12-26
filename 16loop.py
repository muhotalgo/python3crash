# while문
# 조건을 만족할때까지 반복을 실행
# 변수 = 초기값
# while 조건식:
# 	반복할문장
# 	변수증가/감소

# 1 ~ 10 까지 모든 정수 출력
# for i in range(1, 10+1):
#   print(i, end=' ')
i = 1           # 반복초기값
while i <= 10:  # 반복 종료 조건
    print(i, end=' ')
    i = i + 1   # 반복 증감

# 1 ~ 50까지 모든 정수 중 홀수만 출력
i = 1
while i <= 50:
    if i % 2 != 0: print(i, end=' ')
    i = i + 1


# 1 ~ 50까지 모든 정수 중 7의 배수만 출력
i = 1
while i <= 50:
    if i % 7 == 0: print(i, end=' ')
    i = i + 1

# 1 ~ 200까지 모든 정수의 합 출력
i = 1
sum = 0

while i <= 200:
    sum = sum + i
    i = i + 1

print(sum)

# 1 ~ 100 까지 정수 중 3과 8의 공배수와 채소공배수 출력하기
i = 1
mincm = 0

while i <= 100:
    if i % 3 == 0 and i % 8 == 0:
        print(f'공배수 : {i}')
        if mincm == 0: mincm = i    # 최소공배수 저장
    i = i + 1

print(f'최소공배수 : {mincm}')

# 반복문 내 실행 중지 : break
# for, while문 내에서 반복흐름을 벗어나기 위해 사용

# 1 ~ 10000 까지의 정수 합을 출력
# 단, 정수 합이 12345678보다 크면 계산을 중단하세요

# for 문
sum = 0

for i in range(1, 10000):
    if sum > 12345678:
        print(i, sum)
        break               # 반복 중단!
    sum = sum + i

# while 문
i = 1
sum = 0

while i <= 10000:
    if sum > 12345678:
        print(i, sum)
        break
    sum = sum + i
    i = i + 1

# 반복문 내 실행 건너뛰기 : continue
# for, while문 내에서 반복흐름을 일시적으로 넘기기 위해 사용

# 1 ~ 100 까지의 정수 합을 출력
# 단, 3의 배수나 7의 배수는 제외하고 합을 계산하세요

sum = 0

for i in range(1, 100+1):
    if i % 3 == 0 or i % 7 == 0: continue
    sum = sum + i

print(sum)

i = 0
sum = 0

while i < 100:
    i = i + 1
    if i % 3 == 0 or i % 7 == 0: continue
    sum = sum + i

print(sum)

# 1 ~ 99 사이에서 3/6/9가 있으면 짝!이라 출력하기


#
for i in range(1, 100):
    idx = str(i)
    if idx[0] == '3' or idx[0] == '6' or idx[0] == '9':
        idx = idx + '  짝!'
    if i > 10:
        if idx[1] == '3' or idx[1] == '6' or idx[1] == '9':
            idx = idx + '  짝!'
    print(idx)


# 간단한 방법
for i in range(1, 100):
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == 33 or i ==66 or i ==99: jjak += ' 짝!'
    print(f'{i} {jjak}')

# 1~9: 3, 6, 9는 3의 배수 여부 확인
# 10~99: 각 개별 문자가 3,6,9인지 확인 (즉, 3의 배수)
for i in range(1, 99+1):
    if i <= 9:      # 1 ~ 9 사이 3/6/9
        if i % 3 == 0: print(i, '짝!')
        else: print(i)
    else:           # 10 ~ 99 사이 3/6/9
        print(i, end=' ')
        num1 = int(str(i)[0])
        num2 = int(str(i)[1])
        if num1 % 3 == 0: print(' 짝!', end=' ')
        if num2 != 0 and num2 % 3 == 0: print(' 짝!', end=' ')
        print()


# 오전9시 ~ 오후6시까지 열차 교차시간 알아내기

#
for a in range(0, 540+1):
    if (a % 10 == 0 and a % 25 == 0) or (a % 10 == 0 and a % 30 == 0) or (a % 20 == 0 and a % 30 == 0):
        hour = int(9 + a // 60)
        mnte = a % 60
        print(f'{hour:02d}시 {mnte:02d}분')

#
trainA = 10
trainB = 25
trainC = 30

for m in range(1, 540+1):
    if m % trainA == 0 and m % trainB == 0:
        print(f'{9 + m // 60:02d}시 {m % 60:02d}분 A-B')
    if m % trainB == 0 and m % trainC == 0:
        print(f'{9 + m // 60:02d}시 {m % 60:02d}분 B-C')
    if m % trainA == 0 and m % trainB == 0 and m % trainC == 0:
        print(f'{9 + m // 60:02d}시 {m % 60:02d}분 A-B-C')

# 관리자 로그인 기능

#
for i in range(5):
    psswd = input('관리자 암호를 입력하세요. ')
    if psswd == 'hanbitac':
        print('로그인 됐습니다.')
        break
    elif i == 4: print('로그인 실패!! 횟수 초과!!!')
    else: print('암호를 다시 확인하세요!')

#
logincnt = 1
passwd = 'hanbitac'

while True:
    if logincnt > 5:
        print('로그인 실패!! 횟수 초과!!!')
        break

    pwd = input('관리자 암호를 입력하세요. ')

    if passwd != pwd:
        print('암호를 다시 확인하세요!')
        logincnt += 1
    else:
        print('로그인 되었습니다!')
        break


