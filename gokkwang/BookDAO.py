import os
import sys
import gokkwang.dbinfo2 as dbinfo2

insertsql = 'insert into book (bkname, author, publisher, pubdate, retail, price, pctoff, mileage) ' \
            'values (%s,%s,%s,%s,%s,%s,%s,%s)'
selectsql = 'select bkno, bkname, author, publisher, price from book'
selectonesql = 'select * from book where bkname = %s'
updatesql = 'update book set bkname=%s,author=%s,publisher=%s, pubdate=%s, retail=%s, ' \
            'price=%s, pctoff=%s, mileage=%s, regdate=current_timestamp ' \
            'where bkno = %s'
deletesql = 'delete from book where bkno = %s'


class BookDAO:
    @staticmethod
    def insert_book(bk):
        cursor, conn, rowcnt = None, None, -1
        try:
            cursor, conn = dbinfo2.openConn()

            params = [bk.bkname, bk.author, bk.publisher, bk.pubdate,
                      int(bk.retail), int(bk.price), int(bk.pctoff), int(bk.mileage)]
            cursor.execute(insertsql, params)
            conn.commit()
            rowcnt = cursor.rowcount
        except:
            print('BookDAO - insert_book에서 오류 발생!!')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('예외 내용 :', exc_obj)
            print('예외 종류 :', exc_type.__name__)
            print('예외 위치 :', fname, exc_tb.tb_lineno)
        finally:
            dbinfo2.closeConn(cursor, conn)

        return rowcnt

    @staticmethod
    def select_book():
        cursor, conn = dbinfo2.openConn()

        cursor.execute(selectsql)
        rows = cursor.fetchall()

        dbinfo2.closeConn(cursor, conn)
        return rows

    @staticmethod
    def selectone_book(bkname):
        cursor, conn = dbinfo2.openConn()

        cursor.execute(selectonesql, [bkname])
        row = cursor.fetchone()

        dbinfo2.closeConn(cursor, conn)
        return row

    @staticmethod
    def update_book(bk):
        cursor, conn = dbinfo2.openConn()

        params = [bk.bkname, bk.author, bk.publisher, bk.pubdate,
                  int(bk.retail), int(bk.price), int(bk.pctoff), int(bk.mileage), bk.bkno]
        cursor.execute(updatesql, params)

        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo2.closeConn(cursor, conn)
        return rowcnt

    @staticmethod
    def delete_book(bkno):
        cursor, conn = dbinfo2.openConn()

        cursor.execute(deletesql, [bkno])
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo2.closeConn(cursor, conn)
        return rowcnt
