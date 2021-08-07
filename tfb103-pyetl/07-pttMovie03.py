import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

# Run this process 5 times (5 pages)
for i in range(0, 5):
    res = requests.get(url, headers=headers)
    # print(res.text)

    soup = BeautifulSoup(res.text, 'html.parser')
    # titles = soup.select('a') # Return list
    titles = soup.select('div[class="title"]')

    # Get title and articleUrl
    for titleSoup in titles:
        try:
            title = titleSoup.select('a')[0].text
            articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
            print(title)
            print(articleUrl)
        except IndexError:
            print(titleSoup)
        print('=====')

    # Get new url
    newUrl = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    # print(newUrl)
    url = newUrl