# -*- coding:utf-8 -*-
import itchat
import sys

import requests

reload(sys)
sys.setdefaultencoding('utf8')
import os
apiUrl = 'http://www.tuling123.com/openapi/api'

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    """
免费key
8edce3ce905a4c1dbb965e6b35c3834d
eb720a8970964f3f855d863d24406576
1107d5601866433dba9599fac1bc0083
71f28bf79c820df10d39b4074345ef8c
    :param msg:
    :return:
    """
    data = {
        'key'    : '8edce3ce905a4c1dbb965e6b35c3834d', # 如果这个Tuling Key不能用，那就换一个
        'info'   : '%s' % msg['Text'], # 这是我们发出去的消息
        'userid' : 'wechat-robot', # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    print r
    # 让我们打印一下返回的值，看一下我们拿到了什么
    return r['text']

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()

