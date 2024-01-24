from typing import Optional

import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()
url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
params = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬'
}
response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=params)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.getText)
    print(response.url)
else :
    print(response.status_code)

# #headlines = soup.select("div..")
# @app.get("/")
# def read_root():
#
#
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


