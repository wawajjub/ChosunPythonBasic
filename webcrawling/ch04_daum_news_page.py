import requests
from bs4 import BeautifulSoup
from fnc_news import get_news_info

# URL
# https:// 프로토콜
# news.daum.net.~~ 도메인
# ? 쿼리스트링(서버로 데이터를 전달하는 역할)

page = 1
count = 1
while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    link_list = doc.select("ul.list_news2 a.link_txt")
    # 마지막 페이지 체크!
    # 다음뉴스 : 마지막페이지 이동가능(기사없음)
    if len(link_list) == 0:
        break
    print(f"{page}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    for link in  link_list:
        print(f"{count}===========================================================")
        get_news_info(link["href"])
        count += 1
    page += 1




    
    
    
    
    
    
    
    
    
    
    
    
    
    