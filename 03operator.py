# 수식expression
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 => 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 대입식 : 대입연산자를 이용한 수식 (변수 = 수식)

a = 10
b = 20
c = 30
print(a, b, c)

# 대입식을 한 줄에 나타내려면 ; 를 사용

d = 10; e = 20; f = 30
print(d, e, f)

# 다중 할당 : 여러 변수의 값을 한 번에 할당 - , 를 사용
g, h, i = 10, 20, 30
print(g, h, i)

# 정수 대입시 자릿수를 의미하는 구분자 지정 : _ 을 사용
#j = 1000000000    # 10억
j = 1_000_000_000  # 10억
print(j)

# 상수 정의하기
# 프로그램 실행 중에 언제나 동일한 값을 유지하는 변수
# 상수의 이름은 대문자로
PI = 3.14152
print(PI)

# 산술식 : 산술연산자를 이용한 수식
# 파이썬에서는 //, %, ** 도 지원
print(10 / 3, 10 % 3, 10 // 3)      # 나누기, 나머지, 몫
print(10 ** 1, 10 ** 2, 10 ** 3)     # 지수연산

# 관계식 : 관계연산자(대소, 순서관계)를 이용한 수식
# 수식의 결과는 True, False로 출력
print(10 > 3, 10 <= 3, 10 == 3)

# 논리식 : 논리연산자(논리 합/곱/부정)를 이용한 수식
# 또한, 둘 이상의 논리식이나 관계식으로 구성된 수식
# 논리식의 경우, 수식의 구성에 따라 단축식 평가short-circuit가 가능

# and 연산시 첫번째 수식의 결과가 F면 단축식평가 적용
print(3 > 5 and 2 < 3)
print((5 == 3) & (5 > 3))   # and

# or 연산시 첫번째 수식의 결과가 T면 단축식평가 적용
print(2 < 3 or 3 < 5)
print((5 != 3) | (5 > 3))   # or

# 복합 대입연산자 : 대입연산자와 산술연산자를 결합한 수식
# 보통 수식을 간단히 작성시 사용 - 축약표현
# 변수 = 변수 + 수식 => 변수 += 수식
k = 10
k += 1      # k = k + 1
print(k)

# 연산자 우선순위
# 괄호내 연산자 -> 단항연산자 -> 산술연산자 -> 관계연산자 -> 논리연산자

# 연산자의 부수적인 기능 - 문자열 연산
# + : 문자열 연결concate
# * : 문자열 반복repeat 연결
str1 = 'Hello, '
str2 = 'World!!'
print(str1 + str2)

print(str1 * 3)
print(3 * str2)

# 단, 숫자와 문자열에 + 연산을 시도하면? - 오류발생 -> 형변환 필요
print(123 + '456')      # 오류발생!
print(123 + int('456')) # 문자를 숫자로 변환
print(str(123) + '456') # 숫자를 문자로 변환

# 숫자형과 문자형의 논리 연산
# 0 또는 빈 문자열은 False로 인식
# bool 함수를 이용하면 지정한 값의 논리값을 알수있음

print(bool(0), bool(''))
print(bool(1), bool('abc'))

# 다음 수식의 결과는?
print(0 and 'abc', 1 and 'abc')
print('' or 'abc', '' and 'abc')


