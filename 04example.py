# 1
print('''
*   *    **    ****    ****    *   *        /////  
*   *   *  *   *   *   *   *   *   *       | 0 0 | 
*****  *    *  ****    ****     * *       (|  ^  |)
*   *  ******  *   *   *   *     *         | [_] |) 
*   *  *    *  *    *  *    *    *          -----  
''')

print('''
            +---+       
            |   |       
        +---+---+       
        |   |   |       
    +---+---+---+        /\_/\     -----   
    |   |   |   |       ( ‘ ’ )  / Hello \ 
+---+---+---+---+       (  -  ) <  Junior |
|   |   |   |   |        | | |   \ Coder!/ 
+---+---+---+---+       (__|__)    -----  
''')

# 2

# 3
rate1 = ''
# 1stPlayer  = ''
# myprogram.java = ''
long = ''
TimeLimit = ''
numberOfWindows = ''

# 변수로 사용 가능한 것
print(rate1, long, TimeLimit, numberOfWindows)

# 학생 테이블의 각 컬럼 데이터도 변수로 선언하고 초기화
# 변수를 선언하고 값으로 초기화

stno = 1
hakbun = 201350050
name = '김태희'
addr = '경기도 고양시'
birth = '1985.3.22'
deptid = 1
profid = 4
regdate = ('2023-12-20 13:43:15')

print(stno, hakbun, name, addr, birth)
print(stno, deptid, profid, regdate)

# 4

x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8

print(3 * x, 3 * x + y, (x + y) / 7, ( 3 * x + y ) / z + 2 )
print( s0 + v0 * t + 1 / 2 + 1 / 2 * g * t ** 2 )


# 3x
# x = 2.5
# y = 1.5
# m = 18
# n = 4



# 5
print(1 / 3, (1 / 3) * 3)       # 부동소수점 연산의 헛점이 원인
print(7 / 3, 7 % 3, 7 // 3)

result = 2
result /= 2     # result = result / 2
print(result)

# 6
x, y, m, n = 2.5, 1.5, 18, 4
print( x + n * y - (x + n) * y )            # -1.25
print( m / n + m % n )                      # 6.5
print( 5 * x - n / 5 )                      # 11.7
print( 1 - (1 - (1 - (1 - (1 - n)))) )      # -3

# 7

print(3 + 4.5 * 2 + 27 / 8)                             # 15.375
print(True or (False and 3 < 4) or not (5 == 7))        # True
print(True or (3 < 5 & 6 >= 2))                         # True

# 논리연산이 가능하도록 bool 함수 사용
print(not True > bool('A'))                             # True
print(7 % 4 + 3 - 2 / 6 * bool('Z'))                    # 5.666666...
print(bool('D') + 1 + bool('M') % 2 / 3)                # 2.333333...
print(5.0 / 3 + 3 / 3)                                  # 2.6666
print(53 % 21 < 45 / 18)                                # False
print((4 < 6) or True and False or False & (2 > 3))     # True
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))                # -59

# 9
print(True and False and True or True)
# True
print(True or True and True and False)
# True
print((True and False) or (True and not False) or (False and not False))
# True
print((2 < 3) or (5 > 2) and not(4 == 4) or 9 != 4)
# True
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)
# True

# 10

print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)
print(23 / 5 + 23 / 5.0)
print(2.0 + bool('a'))

print(2 + bool('a'))                # 문자와 숫자 간 산술 연산 불가

print(bool('a') / bool('b'))        # 문자끼리 산술 연산 불가
print(float(bool('a') / bool('b')))

print('a' + 'b')

# 논리식과 산술식이 결합된 수식에서는
# 논리식의 결과가 True라면 값이 출력
# 논리식의 결과가 False라면 False가 출력
print((3 < 4) and 5 / 8)
print((3 > 4) and 5 / 8)

print('a' and not 'b')


# 11
name = '홍길동'
weight = 32.5
age = 19
print(name, weight, age)


# 12
# K-나이
# 세는나이 : 출생시 1살, 해가 지나면 +1
# 만나이 : 출생시 0살, 해가 지나면 +1
# 연나이 : 현재년도 - 출생년도

birthYear = 1998
currrentYear = 2023

age = currrentYear - birthYear

print('연나이 : ', age)

# 13

print('''
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
''')



# 구구단 % 서식
gugu = 7


print('%d x 1 = %d' % (gugu, gugu * 1))
print('%d x 2 = %d' % (gugu, gugu * 2))
print('%d x 3 = %d' % (gugu, gugu * 3))
print('%d x 4 = %d' % (gugu, gugu * 4))
print('%d x 5 = %d' % (gugu, gugu * 5))
print('%d x 6 = %d' % (gugu, gugu * 6))
print('%d x 7 = %d' % (gugu, gugu * 7))
print('%d x 8 = %d' % (gugu, gugu * 8))
print('%d x 9 = %d' % (gugu, gugu * 9))



# 구구단 .format 서식


print('{} x 1 = {}'.format(gugu,gugu * 1))
print('{} x 2 = {}'.format(gugu,gugu * 2))
print('{} x 3 = {}'.format(gugu,gugu * 3))
print('{} x 4 = {}'.format(gugu,gugu * 4))
print('{} x 5 = {}'.format(gugu,gugu * 5))
print('{} x 6 = {}'.format(gugu,gugu * 6))
print('{} x 7 = {}'.format(gugu,gugu * 7))
print('{} x 8 = {}'.format(gugu,gugu * 8))
print('{} x 9 = {}'.format(gugu,gugu * 9))



# 구구단 f-string 서식

print(f'{gugu} x 1 = {gugu * 1}')
print(f'{gugu} x 2 = {gugu * 2}')
print(f'{gugu} x 3 = {gugu * 3}')
print(f'{gugu} x 4 = {gugu * 4}')
print(f'{gugu} x 5 = {gugu * 5}')
print(f'{gugu} x 6 = {gugu * 6}')
print(f'{gugu} x 7 = {gugu * 7}')
print(f'{gugu} x 8 = {gugu * 8}')
print(f'{gugu} x 9 = {gugu * 9}')












