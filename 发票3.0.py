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
    shiju = ['诶..朋友们好啊，我是混元形意太极门掌门人——马保国',
             '刚才有个朋友问我马老师发生什么事了，我说怎么回事，给我发了几张截图。',
             '我一看！嗷！原来是昨天，有两个年轻人。',
             '三十多岁，一个体重，九十多公斤，一个体重八十多公斤。',
             '他们说，诶...有一个说是我在健身房练功颈椎练坏了，马老师你能不能教教我浑元功法，诶...帮助治疗一下，我的颈椎病。',
             '我说可以。我说你在健身房练死劲儿，不好用，他不服气。', '诶...我说小朋友，你两个手来折我一个手指头，他折不动。',
             '他说你这也没用。',
             '我说我这个有用，这是化劲儿，传统功夫是讲化劲儿的，四两拨千金。二百多斤的英国大力士，都握不动我这一个手指头啊…哈！',
             '他非要和我试试，我说可以。诶…我一说完他啪就站起来了，很快啊！',
             '然后上来就是一个左正蹬，吭，一个右鞭腿一个左刺拳，我全部防区（口误）防出去了啊！',
             '防出去以后自然是传统功夫以点到为止，右拳放到他鼻子上没打他，我笑一下准备收拳，因为这时间，按传统功夫的点到为止他已经输了。',
             '如果这一拳发力，一拳就把他鼻子打骨折了，放在鼻子上没有打他，他也承认，我先打到他面部。他不知道拳放在他鼻子上，他承认我先打到他面部，啊！',
             '我收拳的时间不打了，他突然袭击，左刺拳来打我脸，啊，我大意了啊，没有闪，诶…他的左拳给我眼，啊，右眼，蹭了一下，但没关系啊！',
             '他也说，啊他截图也说了，两分多钟以后，当时流眼泪了，捂着眼，我说停停。然后两分钟...钟以后，两分多钟以后诶就好啦，我说小伙子你不讲武德你不懂，我说马老师对不...对不起，我不懂规矩。',
             '啊，我是…他说他是乱打的，他可不是乱打的啊，正蹬鞭腿左刺拳，训练有素，后来他说他练过三四年泰拳。啊，看来是，有备而来！',
             '这两个年轻人不讲武德，来骗！来偷袭，我六十九岁的老同志。这好吗？这不好！',
             '我劝！这位年轻人好自为之，好好反思，以后不要再犯这样的聪明，小聪明，啊，呃…武林要以和为贵，要讲武德，不要搞窝里斗。',
             '谢谢朋友们']
    x = shiju[random.randint(0,17)]
    headers = {
        'Connection': 'close','Accept': 'application/json, text/javascript, */*; q=0.01','DNT': '1','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://www.yiban.cn','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.yiban.cn/my/publishvote','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5,zh-TW;q=0.4,da;q=0.3,ht;q=0.2,tr;q=0.1',
        'Cookie': 'UM_distinctid=1738612b52c3d2-0bc865594f06bc-b7a1334-151800-1738612b52d4d0; MESSAGE_NEW_VERSION=1; preview_hidden=0; yiban_user_token=31de6456288de4ab9b809e871e968250; waf_cookie=428c479f-2111-49c6dc07308691c7515f96ba4510db14e5f1; YB_SSID=6b21a0b70ded7e5d300f818cac9f670d; CNZZDATA1253488264=1167475122-1595677764-%7C1605108871; timezone=-8; _cnzz_CV1253488264=%E5%AD%A6%E6%A0%A1%E9%A1%B5%E9%9D%A2%7C%3A%2FIndex%2FMy%2Fpublishvote%7C1605111563376%26%E5%AD%A6%E6%A0%A1%E5%90%8D%E7%A7%B0%7C%E5%85%B6%E4%BB%96%7C1605111563376'
    }
    toupiao_data = {                                                                                                                                                                                                                                                                                                                                                                                                            #选项一的值          #选项二的值
        'puid': '12792328', 'scope_ids': '1000680', 'title': x, 'subjectTxt': 'x', 'subjectPic': '','options_num': '2', 'scopeMin': '1', 'scopeMax': '1', 'minimum': '1', 'voteValue': '2021-06-17 21:55','voteKey': '2', 'public_type': '0', 'isAnonymous': '1', 'voteIsCaptcha': '0', 'istop': '1', 'sysnotice': '2','isshare': '1', 'rsa': '1', 'dom': '.js-submit', 'group_id': '1000680', 'subjectTxt_1': shiju[random.randint(0,17)],'subjectTxt_2': shiju[random.randint(0,17)],
        'captcha': yzm
    }
    r = requests.post(url='https://www.yiban.cn/vote/vote/add', headers=headers, data=toupiao_data)
    if('200' in r.text):
        print('成功发起投票')


for i in range(0,100000):
    yiban_check_ma()
