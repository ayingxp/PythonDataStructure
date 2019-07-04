# -*- coding: utf-8 -*-

import requests

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': '__jsluid_s=d4a756b0b2fdd56cb9c0a91d56139453; __jsl_clearance=1562249334.528|0|QdObFyvIcOcG3QTA0aUL3Yh3kzo%3D; JSESSIONID=KuG9VqXmJb4Hqat45AfWGYMUoxRz8ZQymoO1o5gBLnTbrUOadOLx!928386074; Hm_lvt_cffa7b8af8f70e3fbc35d2763e6dfec9=1562249361; Hm_lpvt_cffa7b8af8f70e3fbc35d2763e6dfec9=1562249361',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}

url = 'https://www.csc108.com/kyrz/kcdbzjList.json?curPage=1&pageSize=10000&stkCode=&market=&enable='

response = requests.get(url, headers=headers)

print response
print response.text