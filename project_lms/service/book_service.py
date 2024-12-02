# 프론트엔드 - contorller - service - DAO - DB
# streamlit - main.py    - service       - DB

# 서비스층 : 실제 비지니스로직의 기능을 담당

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
# 검색
def search_books(keyward: str):
    pass

# 등록
def insert_book(book: dict):
    pass

# 수정
def update_book(book: dict):
    pass

def delete_book(book_isbn: dict):
    pass