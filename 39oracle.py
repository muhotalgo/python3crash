# oracle 클라이언트 라이브러리 설치
# oracle.github.io/odpi/doc/installation.html#windows
# cx-oracle.readthedocs.io/en/latest/user_guide/installation.html

# 주의!
# 오라클 인스턴스 클라이언트 라이브러리 버젼과
# visual studio C++ 재배포 버젼이 일치해야 제대로 실행됨!
# For Instant Client 19 => install VS 2017.
# For Instant Client 18 or 12.2 => install VS 2013

# 오라클디비로 데이터 다루기 1 - select
# pymysql 모듈을 먼저 설치해야 함 - pip install cx_Oracle

# 1) Oracle instant client 버젼에 따라 VS 재배포 패키지 설치
# 2) Oracle instant client를 다운로드하고, c:/Java에 압축해제
# 3) Oracle instant client 설치경로를 시스템의 PATH 환경변수에 등록
# 4) 그런 다음, IntelliJ IDE를 다시 시작

# For Instant Client 21 install VS 2019 or later.
# For Instant Client 19 install VS 2017.
# https://www.oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html

# intelliJ에서 오라클 디비서버로 csv 파일 가져오기 시
# 텍스트 컬럼은 자동으로 CLOB 타입으로 설정
# CLOB가 꼭 필요한 컬럼을 제외하고 varchar 타입으로 바꿀것을 추천!


import cx_Oracle

host = '3.36'
userid = ''
passwd = ''
sid = 'FREE'

# 디비 서버에 연결
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = 'select first_name, last_name from employees'
cursor.execute(sql)

for fname, lname in cursor:
    print(fname, lname)

cursor.close()
conn.close()

# 국가별 메달별 획득수 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = (' select Country, Medal, count(Country) as Cnt from summermedals2 '
       ' group by Country, Medal order by Cnt Desc; ')
cursor.execute(sql)

result = ''
while True:
    row = cursor.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]} {row[2]}\n'

print(result)

cursor.close()
conn.close()

# 승선위치별(embarked) 성별(sex) 생존자(survived) 수 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = (" select embark_town, sex,  count(Alive) alives from titanic2 " \
       " where alive = 'yes' " \
       " group by embark_town, sex " \
       " order by embark_town, sex; ")
cursor.execute(sql)

result = ''
while True:
    row = cursor.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]} {row[2]}\n'

print(result)

cursor.close()
conn.close()

# 승선위치별(embarked) 사람별(who) 생존자(survived) 수 조회 / 남자어른, 여자어른, 남자아이, 여자아이 ..
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = (' select embark_town, who,  count(who) alives from titanic2 ' \
       ' group by embark_town, who ' \
       ' order by embark_town, who; ')
cursor.execute(sql)

result = ''
while True:
    row = cursor.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]} {row[2]}\n'

print(result)

cursor.close()
conn.close()
