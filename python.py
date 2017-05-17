# -*- coding:utf-8 -*-

import urllib2   
import ssl
from cons import *
import json
from send import *

city = {}  #将城市从字符中进行分割
for i in city_name.split('@'):
    if i:
        city[i.split('|')[1]] = i.split('|')[2]

ssl._create_default_https_context = ssl._create_unverified_context #关闭证书认证

train_date = # ex:'2017-05-10'
from_city = # for a city name  ex:  '长沙'
to_city = #  ex:   '成都'
from_station = city[from_city]
to_station = city[to_city]

headers = {   #模拟浏览器，输入头信息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
     'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
}   

def getlist():  #获取数据并处理成json
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station))
    req.headers = headers
    html = urllib2.urlopen(req)
    dict = json.loads(html.read())
    return dict

for i in getlist()['data']['result']:
    #for n in i.split('|'):
    n = i.split('|')[28]
    print n
    if n == u'有'or int(n) > 0:
        print '有余票,可以下单'
        print send_tel('1351*******') //your phone num    this is a API for alidayu 
        break
            #with open('1.txt','a') as fn:      # You need to climb down all the cities in 12306 miles.  i test it for 28
            #fn.write(n.encode('gbk')+'\n')     # 
