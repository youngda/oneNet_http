# -*- coding:utf-8 -*-
# File: http_put.py
#向平台已经创建的数据流发送数据点
import urllib2
import json

def http_put():
    url='http://api.heclouds.com/devices/<设备id>/datapoints'
    values={'datastreams':[{"id":"<数据流id>","datapoints":[{"at":"2016-05-04T15:44:36","value":"71"}]}]}

    jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
    request = urllib2.Request(url, jdata)
    request.add_header('api-key', '<注册得到的key>')
    request.get_method = lambda:'POST'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_put()
print resp
