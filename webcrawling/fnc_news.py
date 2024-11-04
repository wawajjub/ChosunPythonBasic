import requests
from bs4 import BeautifulSoup

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