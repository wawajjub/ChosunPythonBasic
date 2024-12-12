# 도서 관리 시스템
# 1. 도서기능 한정으로 개발
# 2. CRUD 개발 학습

# 프로그래밍 언어 + database
# Create : 데이터 저장
# Read   : 데이터 조회
# Update : 데이터 수정
# Delete : 데이터 삭제

# streamlit run project_lms/main.py

import streamlit as st 
import pandas as pd 
from service import book_service

# 1. 프로그램 초기 설정

st.set_page_config(
    page_title="도서관리 시스템",
    page_icon="project_lms/img/book.png"
)

# 1-1. streamlit 세션상태어세 현재 페이지를 추적하기 위한 상태값을 저장 
# session_state: 웹페이지의 현재 상태값을 저장
# -> session_state값에 page가 없으면 기번적으로 main을 저장
#       = main 페이지 실행
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# 1-2. 다른페이지로 이동하는 함수
def navigate_to(page):
    st.session_state["page"] = page
    st.rerun()
    
# 1-3. 기본 디자인 작업(css)

st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 55rem !important;
        }
        hr {
            margin: 0;
            padding: 0;
        }
        .stButton>button {
            width: 5rem;
            padding: 0;
            margin: 0;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        .stColumns {
            gap: 0px; /* 열 간의 기본 간격을 없애기 */
        }
    </style>
""", unsafe_allow_html=True)

# 2. HEADER
st.title("도서관리 시스템")
st.markdown("<hr>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("HOME"):
        navigate_to("main")
with col2:
    if st.button("등록"):
        navigate_to("insert")
st.markdown("<hr>", unsafe_allow_html=True)

# 3. BODY
def main_page(): # 조회, 검색, 삭제
    # [전체 데이터 조회]
    rows = book_service.get_books()
    # st.dataframe → streamlit에서 표형태로 출력
    
    # [데이터 검색]
    with st.form("search_from"):
        key_ward = st.text_input("도서검색")
        submitted = st.form_submit_button("검색")
        if submitted:
            rows = book_service.search_books(key_ward)
            st.write(f'"{key_ward}"로 검색 된 결과는 총 {len(rows)}건 입니다.')

    event = st.dataframe(rows, 
                         on_select="rerun",
                         selection_mode="single-row",
                         use_container_width=True,
                         hide_index=True)
    
    if len(event.selection["rows"]):
        selected_idx = event.selection["rows"][0] # 선택한 Dataframe의 인덱스 값
        
        # 등록과 달리 수정과 삭제는 
        # 사용자가 기존에 입력한 정보값이 필요함.
        # → 선택한 행의 값을 가져오기
        data = {
            "book_isbn": rows.iloc[selected_idx]["book_ISBN"],
            "book_name": rows.iloc[selected_idx]["book_name"],
            "book_writer": rows.iloc[selected_idx]["book_writer"],
            "book_publisher": rows.iloc[selected_idx]["book_publisher"],
            "book_price": rows.iloc[selected_idx]["book_price"],
            "register_at": rows.iloc[selected_idx]["register_at"],
            "useyn": rows.iloc[selected_idx]["useyn"]
        }
        # UPDATE 페이지에서 데이터를 사용하기 위해
        # 싱태정보 저장하는 곳에 값을 저장
        st.session_state["data"] = data

        if st.button("수정"):
            navigate_to("update")        
        if st.button("삭제"):
            book_service.delete_book(data["book_isbn"])
            navigate_to("main")
            # 값이 변경(INSERT, UPDATE, DELETE) → 최신화
        
def insert_page(): # 등록
    with st.form("insert_form"):
        st.write("도서 등록")
        book_name = st.text_input("도서명")
        book_writer = st.text_input("저자")
        book_publisher = st.text_input("출판사")
        book_price = st.text_input("가격")
        submitted = st.form_submit_button("등록")
        
        if submitted:
            book = {
                "book_name":book_name,
                "book_writer":book_writer,
                "book_publisher":book_publisher,
                "book_price":book_price
            }
            book_service.insert_book(book)
            navigate_to("main")
        
def update_page(): # 수정
    with st.form("update_form"):
        row = st.session_state["data"]

        st.write("도서 수정")
        book_isbn = st.text_input("isbn", value=row["book_isbn"], disabled=True)
        book_name = st.text_input("도서명", value=row["book_name"])
        book_writer = st.text_input("저자", value=row["book_writer"])
        book_publisher = st.text_input("출판사", value=row["book_publisher"])
        book_price = st.text_input("가격", value=row["book_price"])
        register_at = st.text_input("입고일자", value=row["register_at"])
        useyn = st.text_input("사용유무", value=row["useyn"])
        submitted = st.form_submit_button("수정")
        if submitted:
            book = {
                "book_isbn":book_isbn,
                "book_name":book_name,
                "book_writer":book_writer,
                "book_publisher":book_publisher,
                "book_price":book_price,
                "register_at":register_at,
                "useyn":useyn
            }
            book_service.update_book(book)
            navigate_to("main")
        
        
if st.session_state["page"] == "main":
    main_page()
elif st.session_state["page"] == "insert":
    insert_page()
elif st.session_state["page"] == "update":
    update_page()
