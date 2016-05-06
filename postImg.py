# -*- coding:utf-8 -*-
# File: http_put.py

import urllib2
import json
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode

def http_put():
    url='http://api.heclouds.com/bindata?device_id=<设备的id>&datastream_id=<数据流id>'
    
    f = open('img.jpg','rb')
    b = f.read()
    f.close()

    request = urllib2.Request(url,b)
    request.add_header('api-key', '注册得到的key')
    request.get_method = lambda:'POST'
    request = urllib2.urlopen(request)
    return request.read()

resp = http_put()
a = eval(resp)
aa = a.get('data')
uuid = aa.get('index')

print resp
