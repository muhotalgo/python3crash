# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

# 입력 데이터 선언
name = '세라믹'
kor = 40
eng = 68
mat = 73

# 성적처리
tot = kor + eng + mat
avg = tot / 3

# 결과 출력
print(f'이름: {name:s}, 국어: {kor}, 영어: {eng}, 수학: {mat}')
print(f'총점: {tot:d}, 평균: {avg:.1f}')
