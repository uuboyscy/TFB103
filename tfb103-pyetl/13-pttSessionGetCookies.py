import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

landingPageUrl = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
askOver18Url = 'https://www.ptt.cc/ask/over18'
pttGossipUrl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# Create session
ss = requests.session()
print(ss.cookies)

# Get form data
resLandingPage = ss.get(landingPageUrl, headers=headers)
soupLandingPage = BeautifulSoup(resLandingPage.text, 'html.parser')
print(ss.cookies)

data = dict()
key1 = soupLandingPage.select('input')[0]['name']
value1 = soupLandingPage.select('input')[0]['value']
data[key1] = value1

key2 = soupLandingPage.select('button')[0]['name']
value2 = soupLandingPage.select('button')[0]['value']
data[key2] = value2

print(data)

ss.post(askOver18Url, headers=headers, data=data)
print(ss.cookies)

res = ss.get(pttGossipUrl, headers=headers)
print(res.text)