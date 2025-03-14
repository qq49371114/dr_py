import re
import json
from security import safe_requests


class AcFun:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }

    def start(self):
        res = safe_requests.get(self.url, headers=self.headers)
        json_info = json.loads(re.findall("window.pageInfo =(.*?);", res.text)[0].split("=", 1)[-1].strip())
        print(json_info)
        return json_info


if __name__ == '__main__':
    AcFun().start()
