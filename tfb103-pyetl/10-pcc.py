import requests
from bs4 import BeautifulSoup

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

dataStr = """method: search
searchMethod: true
searchTarget: ATM
orgName: vcjkzjvl
orgId: vhcxjlzhkv
hid_1: 1
tenderName: chvjhvcxlz
tenderId: chxzKJvc
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/08/07
awardAnnounceEndDate: 110/08/07
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: vhcjxkz
hid_2: 1
gottenVendorName: fhlhafjdks
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

data = dict()
for r in dataStr.split('\n'):
    key = r.split(': ')[0]
    value = r.split(': ')[1]
    data[key] = value

data = {i.split(': ')[0]: i.split(': ')[1] for i in dataStr.split('\n')}
print(data)
