import requests
from bs4 import BeautifulSoup
import lxml
import json


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

totalList=[]

for i in range(8):
    url = 'https://comic.naver.com/api/article/list?titleId=739411&page='+str(i)
    res = ((requests.get(url, headers=headers)).json())['articleList']
    result = map(lambda x: [x['subtitle'],'https://comic.naver.com/webtoon/detail?titleId=739411&no={}'.format(x['no'])], res)

    A=list(result)
    totalList.extend(A)

totalList = [item for sublist in totalList for item in sublist]
print(totalList)