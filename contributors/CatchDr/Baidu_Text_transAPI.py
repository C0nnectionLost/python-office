import requests
import random
from hashlib import md5
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def baidu_trans(query,from_lang,to_lang,appid,appkey):
    # Set your own appid/appkey.


    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    # from_lang = 'en'
    # to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

    # Generate salt and sign

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    if len(result)==3:
        return result['trans_result'][0]['dst']
    else:
        return result

# if __name__ == '__main__':
#     # 百度官方通用翻译api
# 可参考这个链接申请 https://superdoctranslator.com/appidkey
#     appid = 'xxxxxxxxxxxxxxx'
#     appkey = 'xxxxxxxxxxxx'
#     res=baidu_trans("good","en","zh",appid,appkey)
#     print(res)