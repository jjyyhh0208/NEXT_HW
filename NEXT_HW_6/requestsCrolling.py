from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook
from datetime import datetime

url = "https://news.hada.io/"

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    
    if response.status_code == 200:
        html_text = response.text
        
        soup = bs(response.text, 'html.parser')
        
        titles = soup.find_all(class_ = 'topictitle')
        titles = list(map(lambda x: x.text.strip(), titles))
        print(titles)
        
        contents = soup.select('.topicdesc > a')
        contents = list(map(lambda x: x.text, contents))
        
        infos = soup.find_all(class_ = 'topicinfo')
        infos = list(map(lambda x: x.text, infos))
        
        wb = Workbook()
        ws = wb.active
        
        ws.append(["번호", "제목", "내용", "글정보"])
        
        for i, (title, content, info) in enumerate(zip(titles, contents, infos), start=1):
            ws.append([i, title, content, info])
        
        today = datetime.now().strftime('%Y%m%d')
        
        filename = f'dev_article_{today}.xlsx'
        wb.save(filename)
        print(f"엑셀 파일 저장 완료: {filename}")
        
    else:
        print(f"Error: HTTP 요청 실패. 상태 코드: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Error: 요청 중 오류 발생. 오류 메시지: {e}")