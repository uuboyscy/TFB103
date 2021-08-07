import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

res = requests.get(url, headers=headers)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# titles = soup.select('a') # Return list
titles = soup.select('div[class="title"]')
'''
titleSoup will be like 
<div class="title">
<a href="/bbs/movie/M.1628165245.A.D64.html">[情報] 薄荷糖4K數位修復版全台上映戲院公告</a>
</div>
'''
for titleSoup in titles:
    title = titleSoup.select('a')[0].text
    articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
    print(title)
    print(articleUrl)
    print('=====')