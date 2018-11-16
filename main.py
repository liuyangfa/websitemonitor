# -*- coding:utf-8-*-

import logging.config
import sys

from collect.collector import getcitys,checkavailable
from workdata.workdata import works

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    city = getcitys()
    logging.info("当前获取到的城市列表: %s" % city)
    result = int(checkavailable())
    logging.info("监测网站可用次数为%d" % result)
    if result / 10 >= 2:
        works()
        logging.info("监测网站剩余可用次数为%d" % int(checkavailable()))
    else:
        logging.info("监测网站剩余可用次数为%d" % result)


if __name__ == '__main__':
    log_filename = "collect.log"
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='a',
                        filename=log_filename)
    main()
