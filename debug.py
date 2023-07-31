import json

import requests
from pycookiecheat import chrome_cookies

ip = input('输入ip: ')

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

prehosts = [
    {
        "ip": ip,
        "port": 8000
    },
]
payload = {
    'description': 'debug',
    'deadline': 1,
    'prehosts': str(prehosts),
    'host': str([ip, ])
}

cookie = chrome_cookies('https://npsp.alibaba-inc.com/paas/onlinedebug/submit.json')

resp = requests.post('https://npsp.alibaba-inc.com/paas/onlinedebug/submit.json', headers=headers, data=payload,
                     cookies=cookie)
text = resp.text
print(text)
