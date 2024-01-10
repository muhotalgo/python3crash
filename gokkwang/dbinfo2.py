import oracledb
import pymysql  # mysql
import os

# 시스템 환경변수 등록
# linux : export 키=값
# windows : set 키=값

url = os.getenv('MURL')
userid = os.getenv('ID')
passwd = os.getenv('PW')
dbname = os.getenv('DBNM')
# sid = os.getenv('sid')



def openConn():
    """
    데이터베이스 커서와 커넥션 객체 생성
    :return: 커서, 커넥션 객체 반환
    """
    conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')
    cur = conn.cursor()

    return cur, conn


def closeConn(cur, conn):
    """
    데이터베이스 커서와 연결 종료
    :param cur: 접속중인 커서 객체
    :param conn: 접속중인 커넥션 객체
    :return: 없음
    """
    cur.close()
    conn.close()
