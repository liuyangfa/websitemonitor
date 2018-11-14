# -*- coding:utf-8-*-

import sys
import json
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


def get_data(url, code):
    resp = requests.get("%s%s" % (url, code))
    if resp.status_code != 200:
        return "ERROR"
    content = json.loads(resp.content.replace("update_" + code + "(", "").replace(")", "")).get("result")
    status = content['message']
    country = content['cp_country']
    city = content['cp_city']
    if status != 'OK':
        print country + " " + city + ": " + status
        rtime = 0
        ctime = 0
        dtime = 0
    else:
        rtime = content['rtime']  # 解析时间
        ctime = content['ctime']  # 链接时间
        dtime = content['dtime']  # 下载时间
    print "%s\t%s %s\t%s\t%s\t%s" % (status, country, city, rtime, ctime, dtime)
    return (country, city, rtime, ctime, dtime)
