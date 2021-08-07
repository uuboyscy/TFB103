from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

# Get HTML string
html = res.read().decode('utf-8')
# print(html)

# Transform HTML string to BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# This will return a List object
logo = soup.findAll('a', {'id': 'logo'})
logo = soup.findAll('a', id='logo')
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc' + logo[0]['href'])

content = soup.findAll('div', class_='bbs-content')
print(content)

board = content[0].findAll('a', class_='board')
print(board)

print()
print(type(soup))
print(type(content[0]))



