from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from collect_dao import insert_news
import requests
import pandas as pd

options = Options()
options.add_argument("disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("detach", True)
options.add_argument("headless")

def collect_news():    
    driver = webdriver.Chrome(options=options)
    url = "https://news.daum.net/home" # 다음뉴스 홈
    driver.get(url)
    time.sleep(1)
    
    count = 0 
    url_list = []
    collect_list = [] # 뉴스 수집 데이터
    flag = 0
    while True:
        doc = BeautifulSoup(driver.page_source, "html.parser")
        # link_list -> 현재 페이지의 수집할 기사 링크(9개)
        # - 현제 페이지 수집완료! -> link 목록을 저장!
        
        # if 현재 링크가 링크 목록에 있는지 확인
        # 있다면 멈추고 없다면 계속 수집
        link_list = doc.select("article.content-article ul.list_newsheadline2 a.item_newsheadline2")
        for link in  link_list:
            # 중복체크
            if link in url_list:
                flag = 1
                break
            print(f"{count}===========================================================")
            # 뉴스 1건의 수집정보
            data = get_news_info(link["href"])
            collect_list.append(data)
            count += 1
            url_list.append(link)
            
        if flag == 1:
            break
        # 다음뉴스 버튼 클릭 이벤트
        driver.find_element(By.XPATH, '//*[@id="58d84141-b8dd-413c-9500-447b39ec29b9"]/div[2]/a').click()
        time.sleep(1)
        
        # collect_list -> 3page x 9기사 = 27개의 기사 수집 정보
        # Python 2차원 데이터 -> "pandas" DataFrame(표) 형태로 변환 사용!
    col_name = ["title", "write", "content", "regdate"]
    df_news = pd.DataFrame(collect_list, columns=col_name)    
    return df_news, count
    
    
    
    
    
    
    
    
    
    
    
        

def get_news_info(url:str): 
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    for text in contents:
        content += text.get_text()
        
    writer_list = doc.select("span.txt_info")
    if len(writer_list) < 2:
        writer = ""
    else:
        writer = writer_list[0].get_text()
        
    writer = writer_list[0].get_text()    
    reg_date = doc.select("span.num_date")[0].get_text()
    split_list = reg_date.split(".") 
    spilt_data = list(map(lambda x: x.strip(), split_list))
    reg_date = spilt_data[0] + spilt_data[1] + spilt_data[2]
    print(f"뉴스 제목: {title}")
    print(f"뉴스 기자: {writer}")
    print(f"뉴스 날짜: {reg_date}")
    print(f"뉴스 본문: {content}")
    
    data = {
        "title": title,
        "writer": writer,
        "content": content,
        "regdate": reg_date
    }
    insert_news(data)
    
    return data