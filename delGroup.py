from urllib.request import urlopen
import urllib.request
import json
import requests

headers = { 
    "accept":"application/json, text/javascript, */*; q=0.01",
	'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
	'Referer':'http://www.qq.com/',
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"" #cookie自行抓包
	}

count = 0

while count<22: #循环22次
    count = count+1    
    data = {"gc":"",#群号
        "st":"0",
        "end":"20",
        "sort":"0",
        "bkn":"" #自行抓包
    }
    bytes = urllib.parse.urlencode(data).encode('utf-8')
    url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
    req = urllib.request.Request(url, bytes,headers = headers,method='POST')
    resp = urllib.request.urlopen(req).read().decode("utf-8")
    dic = json.loads(resp)
    mems = dic['mems']
    ul = ''
    for mem in mems:
        u = mem['uin']
        if u == 505413434:
            continue
        ul = ul+str(u)+"|"
    ul = ul[0:len(ul)-1] 
    deleUrl = 'https://qun.qq.com/cgi-bin/qun_mgr/delete_group_member'
    data = {"gc":"", #群号
        "flag":"0",
        "ul":ul,
        "bkn":"" #自行抓包
    }    
    bytes = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(deleUrl, bytes,headers = headers,method='POST')
    resp = urllib.request.urlopen(req).read().decode("utf-8")
    print(resp)

