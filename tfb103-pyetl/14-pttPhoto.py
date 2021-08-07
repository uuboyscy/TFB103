import requests
import json

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=236646571'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

res = requests.get(url, headers=headers)

# print(res.text)
## This is a List
## each object(Dict) in it is an article
## id -> article url
## title -> title
## mediaMeta -> images(list)
jsonData = json.loads(res.text) # return list/dict
# for r in jsonData:
#     print(r)
# print(jsonData[0].keys())
# for k in jsonData[0]:
#     print(k)
#
# print(jsonData[1]['mediaMeta'])
# for i in jsonData[1]['mediaMeta']:
#     print(i['url'])

for articleDict in jsonData:
    title = articleDict['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p/' + str(articleDict['id'])
    print(title)
    print(articleUrl)
    for imgs in articleDict['mediaMeta']:
        print('\t' + imgs['url'])
    print('=========')