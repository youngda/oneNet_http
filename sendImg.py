# -*- coding:utf-8 -*-
# File: http_put.py
# 向平台发送图片
import urllib2
import json
import time
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode

def http_put():
    url='http://api.heclouds.com/bindata?device_id=<设备id>&datastream_id=<数据流id>'
    
    f = open('img.jpg','rb')
    b = f.read()
    f.close()

    request = urllib2.Request(url,b)
    request.add_header('api-key', '注册得到的key')
    request.get_method = lambda:'POST'
    request = urllib2.urlopen(request)
    return request.read()

def http_put_uuid(uuid):
    url='http://api.heclouds.com/devices/<设备id>/datapoints'
    d = time.strftime('%Y-%m-%dT%H:%M:%S')
    print d
    values={'datastreams':[{"id":"<数据流id>","datapoints":[{"at":d,"value":uuid}]}]}

    jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
    request = urllib2.Request(url, jdata)
    request.add_header('api-key', '<注册得到的key>')
    request.get_method = lambda:'POST'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_put()
a = eval(resp)
aa = a.get('data')
uuid = aa.get('index')
result = http_put_uuid(uuid)
print result
