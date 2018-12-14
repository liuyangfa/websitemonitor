# -*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

codes = {
    "hk": "中国 - 香港特别行政区",
    "d2": "德国 - 慕尼黑",
    "se": "瑞典 - 斯德哥尔摩",
    "uk": "英国 - 伦敦",
    "it": "意大利 - 帕多瓦",
    "ch": "瑞士 - 苏黎世",
    "n4": "荷兰 - 格罗宁根",
    "r1": "美国 - 达拉斯",
    "gr": "希腊 - 雅典",
    "mt": "加拿大 - 蒙特利尔",
}
sites = {
    "dj.platon.network": "Platon(东京)",
    "www.platon.network": "Platon(东南亚)",
    "www.ont.io": "ONT本体(东南亚)",
    "www.ethereum.org": "Ethereum以太坊",
}

countryCode = {
    "cn": "中国",
    "de": "德国",
    "se": "瑞典",
    "gb": "英国",
    "it": "意大利",
    "ch": "瑞士",
    "nl": "荷兰",
    "us": "美国",
    "gr": "希腊",
    "ca": "加拿大"
}

cityCode = {
    "Hong Kong": "香港",
    "München": "慕尼黑",
    "Stockholm": "斯德哥尔摩",
    "London": "伦敦",
    "Padova": "帕多瓦",
    "Zurich": "苏黎世",
    "Groningen": "格罗宁根",
    "Dallas": "达拉斯",
    "Athens": "雅典",
    "Montreal": "蒙特利尔",
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
