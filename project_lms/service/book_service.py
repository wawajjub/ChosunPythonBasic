# 프론트엔드 - contorller - service - DAO - DB
# streamlit - main.py    - service       - DB

# 서비스층 : 실제 비지니스로직의 기능을 담당

# MVC, MVT 패턴
# 시스템 개발시 사용하는 패턴 

# 웹 브라우저 요청: http://naver.com/cafe
#       ↓
#    웹 서버(네이버 서버)
# 1. 컨트롤러: 요청을 받아서 해당 로직을 처리할 수 있는 서비스로 전달하는 역할   
#       → cafe 관련 서비스로 전달
# 2. 서비스: 실제 비지니스 로직을 처리하는 곳
#       → cafe 글쓰기 관련 함수로 처리 
#       → 함수를 처리하는 도중에 DB가 필요한 경우 DAO로 전달
# 3. DAO(Data Access Object): DB관련 로직을 처리
#       → cafeDAO를 사용해서 SQL 실행
#       → DB로부터 전달받은 결과를 서비스로 전달  
# 4. 서비스
#       → DAO로부터 처리받은 결과를 컨트롤러로 전달
# 5. 컨트롤러
#       → 서비스로부터 처리받은 겨과를 웹 브라우저에게 전달

# 겨울방학 추천코스
# 1. SQLD 자격증
# 2. 웹 개발 공부
#   → 모든 IT의 정수
#   → Python 웹 프레임워크: Django(추), Flask(비추), FastAPI
#   파이썬 웹개발자 취업 → 어렵고 잘 안씀

# 1등:SprintBoot(java)
# 2등:Node.js(javascript)
# 3등:Django(python)
# ※ 나는 졸업 전에 취업하고 싶다 → springboot
# ※ HTML, CSS, JS(기본) → 1달 공부
# ※ 토이프로젝트, 사이드프로젝트, 펫프로젝트
#   → 개인 웹 사이트

from common.connection import connection
import pandas as pd


# 도서목록 조회(all)
def get_books():
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            SELECT * FROM tbl_book;
        """
        curs.execute(sql)
        # 전체결과 → dict파일
        rows = curs.fetchall() #실행결과 전체받기
        # dict 데이터 → 표로 전환
        rows = pd.DataFrame(rows)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows

# 검색
def search_books(keyward: str):
    conn = connection()
    
    try:
        curs = conn.cursor()
        sql = """
            SELECT * 
            FROM tbl_book 
            WHERE book_name LIKE %(keyward)s
            OR book_writer LIKE %(keyward)s
            OR book_publisher LIKE %(keyward)s
        """
        curs.execute(sql, {"keyward": "%"+keyward+"%"})
        rows = curs.fetchall()
        rows = pd.DataFrame(rows)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows

# 등록
def insert_book(book: dict):
    conn = connection()
    
    try:
        curs = conn.cursor()
        sql = """
            INSERT INTO tbl_book(book_name, book_writer, book_publisher, book_price)  
            VALUES(%(book_name)s,%(book_writer)s,%(book_publisher)s,%(book_price)s);
        """
        curs.execute(sql, book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()

# ※ UPDATE문과 DELETE문은 WHERE절과 함께 사용할 것 !★★★★★!

# 수정
def update_book(book: dict):
    conn = connection()
    
    try:
        curs = conn.cursor()
        sql = """
            UPDATE tbl_book 
            SET book_name = %(book_name)s,
                book_writer = %(book_writer)s,
                book_publisher = %(book_publisher)s,
                book_price = %(book_price)s,
                register_at = %(register_at)s,
                useyn = %(useyn)s
            WHERE book_ISBN = %(book_isbn)s;
        """
        curs.execute(sql, book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()

def delete_book(book_isbn: str):
    conn = connection()
    
    try:
        curs = conn.cursor()
        sql = """
            DELETE FROM tbl_book
            WHERE book_ISBN = %(book_isbn)s;
        """
        curs.execute(sql, {"book_isbn": book_isbn})
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()