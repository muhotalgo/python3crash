import json
import sys
from collections import OrderedDict

emps = {'response': {'body': {'totalCount': 0, 'items': []}}}
items = []


# 사원 관리 프로그램 초기화
def load_employees():
    """
    사원 관리 프로그램 초기화 함수
    :return: 없음
    """
    print('프로그램을 초기화합니다...')
    global emps
    global items

    try:  # 만일 작업 중에 오류가 발생하면
        with open('employees.json') as f:
            emps = json.load(f)
            items = emps['response']['body']['items']
    except:
        items = emps['response']['body']['items']

    print('프로그램이 성공적으로 초기화되었습니다...')


# 사원 관리 메뉴
def show_menu():
    """
    사원 관리 프로그램 메뉴를 출력하는 함수
    :return: 메뉴
    """
    main_menu = '''
-*--*-- * --*--*--
사원 관리 프로그램 v2
------------------
1. 사원 정보 추가
2. 사원 정보 조회
3. 사원 정보 상세조회
4. 사원 정보 수정
5. 사원 정보 삭제
0. 프로그램 종료
-----------------
'''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


# 사원 추가
def input_employee():
    """
    사원을 추가하는 함수
    :return: 사원
    """
    emp = OrderedDict()
    emp['empno'] = input('사원번호는? ')
    emp['fname'] = input('이름은? ')
    emp['lname'] = input('성은? ')
    emp['email'] = input('이메일은? ')
    emp['hdate'] = input('입사일은? ')
    emp['jobid'] = input('직책은? ')
    emp['sal'] = input('급여는? ')
    emp['deptid'] = input('부서번호는? ')
    return emp


# 사원 정보를 파일에 저장
def save_employee(emp):
    """
    사원 정보를 파일에 저장
    :param emp: 사원 정보
    :return: 없음
    """
    items.append(emp)
    emps['response']['body']['totalCount'] += 1

    with open('employees.json', 'w') as f:
        json.dump(emps, f)


# 사원 정보 추가
def add_employee():
    print('사원 정보를 등록합니다...')
    emp = input_employee()
    save_employee(emp)


# 모든 사원 정보 조회 (사원번호/이름/직책/부서번호)
def read_employee():
    """
    모든 사원의 정보를 조회하는 함수 (사원번호/이름/직책/부서번호)
    :return: 없음
    """
    print('모든 사원 정보를 조회합니다...')
    result = ''
    for emp in items:
        result += (f"사원번호: {emp['empno']}\t이름: {emp['fname']}\t"
                   f"직책: {emp['jobid']}\t부서번호: {emp['deptid']}\n")
    print(result)


# 특정 사원의 상세 정보를 조회
def readone_employee():
    print('특정 사원의 상세 정보를 조회합니다...')
    empno = input('조회할 사원의 사원 번호를 입력하십시오. ')

    info = '존재하지 않는 사원 번호입니다.'
    for emp in emps['response']['body']['items']:
        if emp['empno'] == empno:
            info = (f"사원번호: {emp['empno']}, 이름: {emp['fname']}, 성: {emp['lname']}, "
                    f"이메일: {emp['email']}, 입사일: {emp['hdate']}, 직책: {emp['jobid']}, "
                    f"급여: {emp['sal']}, 부서번호: {emp['deptid']}")
        break

    print(info)


def read_again(data, empno):
    emp = OrderedDict()
    emp['empno'] = empno
    emp['fname'] = input(f'변경할 이름? ({data["fname"]}) : ')
    emp['lname'] = input(f'변경할 성? ({data["lname"]}) : ')
    emp['email'] = input(f'변경할 이메일? ({data["email"]}) : ')
    emp['hdate'] = input(f'변경할 입사일? ({data["hdate"]}) : ')
    emp['jobid'] = input(f'변경할 직책? ({data["jobid"]}) : ')
    emp['sal'] = input(f'변경할 급여? ({data["sal"]}) : ')
    emp['deptid'] = input(f'변경할 부서 번호? ({data["deptid"]}) : ')

    return emp


def flush_employee():
    with open('employees.json', 'w', encoding='UTF-8') as f:
        json.dump(emps, f, ensure_ascii=False)


# 사원 수정
def modify_employee():
    print('특정 사원의 상세 정보를 수정합니다...')
    empno = input('수정할 사원의 사원 번호를 입력하십시오. ')

    data = None
    idx = None
    for i, emp in enumerate(items):
        if emp['empno'] == empno:
            data = emp
            idx = i

    if data:
        data = read_again(data, empno)
        items[idx] = data
        flush_employee()
    else:
        print('존재하지 않는 사원 번호입니다.')


def remove_employee():
    empno = input('삭제할 사원의 사원 번호를 입력하십시오. ')

    data = None
    for emp in items:
        if emp['empno'] == empno:
            data = emp
            break
        else:
            print('존재하지 않는 사원번호입니다.')

    if data:
        confirm = input('정말로 삭제하시겠습니까? (yes/no) : ')
        if confirm == 'yes':
            items.remove(data)
            emps['response']['body']['totalCount'] -= 1
            print(f'{empno}의 데이터가 삭제되었습니다!')
            flush_employee()
        else:
            print(f'삭제가 취소되었습니다!!')


def exit_program():
    print('프로그램을 종료합니다.!')
    sys.exit(0)
