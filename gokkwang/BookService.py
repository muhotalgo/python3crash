import sys

from gokkwang.Book import Book
from gokkwang.BookDAO import BookDAO


# 메뉴 출력
def show_menu():  # 메뉴 출력
    """
    메뉴 출력하고 메뉴항목을 입력받음
    :return: 입력받은 메뉴번호
    """
    main_menu = '''
--------------------
도서관리 프로그램 v1
--------------------
1. 도서 데이터 추가
2. 도서 데이터 조회
3. 도서 데이터 상세조회
4. 도서 데이터 수정
5. 도서 데이터 삭제
0. 프로그램 종료
--------------------
'''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


def input_book():
    bkname = input('도서명은? ')
    author = input('도서 저자는? ')
    publisher = input('도서 출판사는? ')
    pubdate = input('도서 출간일은? ')
    retail = int(input('도서 소매가는? '))
    pctoff = int(input('도서 할인율은? '))

    bk = Book(bkname, author, publisher, pubdate, retail, pctoff)
    bk.price = bk.retail * (1 - (bk.pctoff / 100))
    bk.mileage = bk.retail * (bk.pctoff / 100)

    return bk


# 도서 데이터 추가 (입력-처리-저장)
def new_book():
    """
    도서 데이터 추가 (입력-처리-저장)
    :return:없음
    """
    print('도서 데이터 추가')
    bk = input_book()
    print(bk)

    rowcnt = BookDAO.insert_book(bk)
    print(f'{rowcnt} 건의 도서데이터 등록됨!!')


# 모든 도서 데이터 출력
def read_book():
    """
    모든 도서 데이터 출력 (번호/도서명/저자/출판사/판매가)
    :return: 없음
    """
    print('도서 데이터 조회')
    result = ''

    rows = BookDAO.select_book()
    for row in rows:
        result += f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]:,}\n'

    print(result)


# 도서 데이터 상세 조회
def readone_book():
    """
    도서 데이터 상세 조회하는 함수
    :return: 없음
    """
    bkname = input('상세 조회할 도서명은? ')

    result = ''

    row = BookDAO.selectone_book(bkname)
    if row:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} '
              f'{row[5]:,} {row[6]:,} {row[7]}% {row[8]:,} {row[9]} ')
    else:
        print('데이터가 없어요!')

    print(result)


def reinput_book(obk):
    bkname = input(f'도서명은? ({obk[1]}) ')
    author = input(f'도서 저자는? ({obk[2]}) ')
    publisher = input(f'도서 출판사는? ({obk[3]}) ')
    pubdate = input(f'도서 출간일은? ({obk[4]}) ')
    retail = int(input(f'도서 소매가는? ({obk[5]}) '))
    pctoff = int(input(f'도서 할인율은? ({obk[7]}) '))

    bk = Book(bkname, author, publisher, pubdate, retail, pctoff)

    bk.price = bk.retail * (1 - (bk.pctoff / 100))
    bk.mileage = bk.retail * (bk.pctoff / 100)
    bk.bkno = obk[0]

    return bk


# 도서 데이터 수정
def modify_book():
    """
    도서 데이터 수정하는 함수
    :return: 없음
    """
    bkname = input('수정할 도서이름은? ')
    row = BookDAO.selectone_book(bkname)

    if row:
        bk = reinput_book(row)
        rowcnt = BookDAO.update_book(bk)
        print(f'{rowcnt} 건의 도서데이터 수정됨!!')
    else:
        print('수정할 데이터는 없어요!!')


# 도서 데이터 삭제
def remove_book():
    """
    도서 데이터를 삭제하는 함수
    :return: 없음
    """
    bkno = input('삭제할 도서번호는? ')

    rowcnt = BookDAO.delete_book(bkno)
    print(f'{rowcnt} 건의 도서데이터 삭제됨!!')


# 도서 처리 프로그램 종료
def exit_book():
    """
    도서 처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """

    print('프로그램 종료!')
    sys.exit(0)
