# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 입력 데이터 선언
names = ['소혜', '리키', '쥬스']
kors = [20, 99, 70]
engs = [90, 10, 25]
mats = [99, 60, 85]
tots = []
avgs = []

# 성적처리

# tot = kors[0] + engs[0] + mats[0]
# tots.append(tot)
# tot = kors[1] + engs[1] + mats[1]
# tots.append(tot)
# tot = kors[2] + engs[2] + mats[2]
# tots.append(tot)
#
#
# avg = tots[0] / 3
# avgs.append(avg)
# avg = tots[1] / 3
# avgs.append(avg)
# avg = tots[2] / 3
# avgs.append(avg)

tots.append(kors[0] + engs[0] + mats[0])
tots.append(kors[1] + engs[1] + mats[1])
tots.append(kors[2] + engs[2] + mats[2])

avgs.append(tots[0] / 3)
avgs.append(tots[1] / 3)
avgs.append(tots[2] / 3)


# 결과 출력
# # 소혜
# a = 0; print(f'이름: {names[a]:s}, 국어: {kors[a]}, 영어: {engs[a]}, 수학: {mats[a]}')
# print(f'총점: {tots[a]:d}, 평균: {avgs[a]:.1f}')
#
# # 리키
# a = 1; print(f'이름: {names[a]:s}, 국어: {kors[a]}, 영어: {engs[a]}, 수학: {mats[a]}')
# print(f'총점: {tots[a]:d}, 평균: {avgs[a]:.1f}')
#
# # 쥬스
# a = 2; print(f'이름: {names[a]:s}, 국어: {kors[a]}, 영어: {engs[a]}, 수학: {mats[a]}')
# print(f'총점: {tots[a]:d}, 평균: {avgs[a]:.1f}')


print(f'이름: {names[0]:s}, 국어: {kors[0]}, 영어: {engs[0]}, 수학: {mats[0]}')
print(f'총점: {tots[0]:d}, 평균: {avgs[0]:.1f}')

print(f'이름: {names[1]:s}, 국어: {kors[1]}, 영어: {engs[1]}, 수학: {mats[1]}')
print(f'총점: {tots[1]:d}, 평균: {avgs[1]:.1f}')

print(f'이름: {names[2]:s}, 국어: {kors[2]}, 영어: {engs[2]}, 수학: {mats[2]}')
print(f'총점: {tots[2]:d}, 평균: {avgs[2]:.1f}')






