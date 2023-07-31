from requests.sessions import Session
import browsercookie
import urllib3
import pickle
import re
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HEADERS = {
    "accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    # 'content-type': 'application/json;charset=utf-8',
    "kos-module": "kos-cc",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


class AliSession(Session):
    def __init__(self):
        super(AliSession, self).__init__()
        self.verify = False
        self.headers.update(HEADERS)
        self.cookies.update(browsercookie.chrome())
        self.max_redirects = 10

    def is_400(self, code):
        return int(code) == 400

    def post(self, url, data=None, json=None, **kwargs):
        res = super(AliSession, self).post(url, data, json, **kwargs)
        if self.is_400(res.status_code):
            res = super(AliSession, self).post(url, data, json, **kwargs)
        return res

    def get(self, url, **kwargs):
        res = super(AliSession, self).get(url, **kwargs)
        if self.is_400(res.status_code):
            res = super(AliSession, self).get(url, **kwargs)
        return res

    def close(self):
        pass

    def json(self, response):
        json_data = re.search(r"{.*}", response.text).group()
        return json.loads(json_data)


ali_session = AliSession()

if __name__ == '__main__':
    pass

