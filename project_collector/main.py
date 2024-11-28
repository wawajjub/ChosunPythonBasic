# 다음 뉴스 수집기

# 웹사이트 
#   - 화면: 뉴스 카테고리를 선택(streamlit)
#   - 수집: 뉴스 수집(requests, beautifulsoup) 
#   - 화면: 출력, 엑셀(다운로드)(streamlit, pandas)
#   - 저장: 데이터베이스 저장(pymysql + MariaDB)
from fnc_news import collect_news
import streamlit as st
import re # 정규식

# README.md -> md(Markdown) 문서
# ㄴ emoji(아이콘) -> https://snskeyboard.com/emoji/
# Streamlit Doc -> https://docs.streamlit.io/

# streamlit run project_collector/main.py

def convert_df(df):
    return df.to_csv(index=False, encoding="utf8")


def main():
    st.set_page_config(
        page_title="뉴스 수집기", # 웹사이트의 제목
        page_icon="project_collector/img/favicon.png"            # 웹사이트의 파비콘
    )
    st.title("NEWS: :blue[Collector]")
    st.text("DAUM 뉴스를 수집합니다.")
        
        # 1. 정규식 → 문자만 추출(수사, 특수문자 제거)
        # 2. 수집 데이터를 엑셀로 다운로드
        # 3. README.md 작성! → 프로젝트 정리(Github)
    flag = False # 수집 성공여부
    if st.button("수집"):
        df_news, count = collect_news()
        st.write(f"뉴스 {count}건 수집 완료")
        st.write(df_news)
        flag = True
        news_csv = convert_df(df_news)
                
    if flag:
        st.download_button(
            label="다운로드",
            data=news_csv,
            file_name=f"실시간뉴스.csv",
            mime="text/csv",
            key="download_csv"
        )        
                
                
if __name__ == "__main__":
    main()