import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index%s.html'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

page = 9508

for i in range(0, 5):
    res = requests.get(url%(page), headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('div[class="title"]')
    # for titleSoup in titles:
    #     try:
    #         title = titleSoup.select('a')[0].text
    #         articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
    #         print(title)
    #         print(articleUrl)
    #     except IndexError:
    #         print(titleSoup)
    #     print('=====')

    for titleSoup in titles:
        if titleSoup.select('a').__len__() == 0:
            continue
        title = titleSoup.select('a')[0].text
        articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
        print(title)
        print(articleUrl)
        print('=====')

    page -= 1

