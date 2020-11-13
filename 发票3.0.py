import requests,base64,random

def yiban_check_ma():#请求验证码
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ""(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Cookie': 'UM_distinctid=1738612b52c3d2-0bc865594f06bc-b7a1334-151800-1738612b52d4d0; MESSAGE_NEW_VERSION=1; preview_hidden=0; yiban_user_token=31de6456288de4ab9b809e871e968250; waf_cookie=428c479f-2111-49c6dc07308691c7515f96ba4510db14e5f1; YB_SSID=6b21a0b70ded7e5d300f818cac9f670d; _cnzz_CV1253488264=%E5%AD%A6%E6%A0%A1%E9%A1%B5%E9%9D%A2%7C%3A%2FIndex%2FIndex%2Findex%7C1605109267903%26%E5%AD%A6%E6%A0%A1%E5%90%8D%E7%A7%B0%7C%E5%85%B6%E4%BB%96%7C1605109267904; CNZZDATA1253488264=1167475122-1595677764-%7C1605104607'
    }
    yiban_check_ma_url = "https://www.yiban.cn/captcha/index?Tue%20Dec%2004%202018%2000:01:26%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)"
    r = requests.get(yiban_check_ma_url,headers=headers)
    image_data = base64.b64encode(r.content).decode().replace("\r", "")
    baidu_api(image_data)


def baidu_api(image_data,):#需要传入字符串:image_data
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'#必选参数
    }
    data = {            #base64编码的图片,已去头
        'image':image_data.encode("utf8")
    }
    r = requests.post(url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=24.aa54d48b4888dfaf5ce45fe7df98b6eb.2592000.1607707337.282335-22957927',headers=headers, data=data)
    if('words_result' in r.json() and len(r.json()['words_result'])>=1):
        test_text = r.json()['words_result'][0]['words']
        toupiao(test_text)
    else:
        yiban_check_ma()


def toupiao(yzm):
    #下面是诗
    shiju = ['黄沙百战穿金甲，不破楼兰终不还。',
             '人生自古谁无死？留取丹心照汗青。',
             '落红不是无情物，化作春泥更护花。',
             '海上生明月，天涯共此时。',
             '人面不知何处去，桃花依旧笑春风。',
             '人面不知何处去，桃花依旧笑春风。',
             '去年今日此门中，人面桃花相映红。'
    ]
    headers = {
        'Connection': 'close','Accept': 'application/json, text/javascript, */*; q=0.01','DNT': '1','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://www.yiban.cn','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.yiban.cn/my/publishvote','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5,zh-TW;q=0.4,da;q=0.3,ht;q=0.2,tr;q=0.1',
        'Cookie': 'UM_distinctid=1738612b52c3d2-0bc865594f06bc-b7a1334-151800-1738612b52d4d0; MESSAGE_NEW_VERSION=1; preview_hidden=0; yiban_user_token=31de6456288de4ab9b809e871e968250; waf_cookie=428c479f-2111-49c6dc07308691c7515f96ba4510db14e5f1; YB_SSID=6b21a0b70ded7e5d300f818cac9f670d; CNZZDATA1253488264=1167475122-1595677764-%7C1605108871; timezone=-8; _cnzz_CV1253488264=%E5%AD%A6%E6%A0%A1%E9%A1%B5%E9%9D%A2%7C%3A%2FIndex%2FMy%2Fpublishvote%7C1605111563376%26%E5%AD%A6%E6%A0%A1%E5%90%8D%E7%A7%B0%7C%E5%85%B6%E4%BB%96%7C1605111563376'
    }
    toupiao_data = {                                                                                                                                                                                                                                                                                                                                                                                                            #选项一的值          #选项二的值
        'puid': '12792328', 'scope_ids': '1000680', 'title': shiju[random.randint(0,6)], 'subjectTxt': '', 'subjectPic': '','options_num': '2', 'scopeMin': '1', 'scopeMax': '1', 'minimum': '1', 'voteValue': '2021-06-17 21:55','voteKey': '2', 'public_type': '0', 'isAnonymous': '1', 'voteIsCaptcha': '0', 'istop': '1', 'sysnotice': '2','isshare': '1', 'rsa': '1', 'dom': '.js-submit', 'group_id': '1000680', 'subjectTxt_1': '1','subjectTxt_2': '2',
        'captcha': yzm
    }
    r = requests.post(url='https://www.yiban.cn/vote/vote/add', headers=headers, data=toupiao_data)
    if('911' in r.text or '914' in r.text):
        pass
    elif('200' in r.text):
        print('成功发起投票')


for i in range(0,100000):
    yiban_check_ma()
