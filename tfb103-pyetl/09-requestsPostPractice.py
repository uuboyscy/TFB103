import requests

url = 'https://c6270aae083f.ngrok.io/hello_post'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

data = {
    'username': 'Allen'
}

res = requests.post(url, headers=headers, data=data)

print(res.text)