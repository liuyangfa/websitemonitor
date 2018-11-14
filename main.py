# -*- coding:utf-8-*-

import sys
import xlsxwriter
from collect.collector import *
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

codes = ("hk", "d2", "se", "uk", "it", "ch", "n4", "r1", "gr", "mt")
# # sites = ("www.ont.io", "www.ethereum.org", "www.platon.network", "sg.platon.network")
# sites = {
#     "www.platon.network": "Platon(京东)",
#     "sg.platon.network": "Platon(东南亚)",
#     "www.ont.io": "ONT本体(东南亚)",
#     "www.ethereum.org": "Ethereum以太坊",
# }

sites = {
    "www.platon.network": "Platon(京东)"
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

dates = datetime.today().strftime("%Y%m%d%H%M%S")


def main():
    workbook = xlsxwriter.Workbook(u"PlatON网站服务优化监测表-汇总-%s.xlsx" % (dates))
    titleStyle = workbook.add_format()
    colTitleStyle = workbook.add_format()

    titleStyle.set_bg_color("#00B0F0")
    titleStyle.set_font_name("宋体")
    titleStyle.set_font_size(16)
    titleStyle.set_bold()
    titleStyle.set_top(1)
    titleStyle.set_bottom(1)
    titleStyle.set_right(1)
    titleStyle.set_left(1)
    titleStyle.set_align("center")
    titleStyle.set_align("vcenter")

    colTitleStyle.set_bg_color("#808080")
    colTitleStyle.set_font_name("宋体")
    colTitleStyle.set_font_size(12)
    colTitleStyle.set_bold()
    colTitleStyle.set_bottom(1)
    colTitleStyle.set_top(1)
    colTitleStyle.set_left(1)
    colTitleStyle.set_right(1)
    colTitleStyle.set_align('center')

    areaStyle = workbook.add_format()
    areaStyle.set_font_size(12)
    areaStyle.set_font_name("宋体")

    dataStyle = workbook.add_format()
    dataStyle.set_font_name('Arial')
    dataStyle.set_font_size(10)

    for site in sites.keys():
        # 数据写入行号及列数
        row = 2
        # add_worksheet限制名称不能多于32个字符
        worksheet = workbook.add_worksheet("%s数据" % (sites.get(site)))
        # 设置标题所在行行高
        worksheet.set_row(0, 70)
        # 设置第二列宽度为38个字符,设置第三列到第七列宽度为17个字符
        worksheet.set_column(1, 1, 38)
        worksheet.set_column(2, 6, 17)
        # 合并第1行的第2到7列，并写入标题
        worksheet.merge_range(0, 1, 0, 6, "%s网站服务网页监测例检表%s" % (sites.get(site), dates), titleStyle)

        # 在第二行写入表格的列名
        worksheet.write_string(1, 1, "地区/国家", colTitleStyle)
        worksheet.write_string(1, 2, "访问时间(s)", colTitleStyle)
        worksheet.write_string(1, 3, "解析时间(ms)", colTitleStyle)
        worksheet.write_string(1, 4, "连接时间(ms)", colTitleStyle)
        worksheet.write_string(1, 5, "下载时间(ms)", colTitleStyle)
        worksheet.write_string(1, 6, "访问状态(ms)", colTitleStyle)
        for code in codes:
            country, city, rtime, ctime, dtime = get_data(
                "https://api.asm.ca.com/1.6/cp_check?checkloc=%s&type=https&host=%s&path=&port=443&callback=update_" % (
                    code, site), code)

            worksheet.write_string(row, 1, "%s-%s" % (countryCode.get(country), cityCode.get(city)), areaStyle)
            worksheet.write_number(row, 3, int(rtime), dataStyle)
            worksheet.write_number(row, 4, int(ctime), dataStyle)
            worksheet.write_number(row, 5, int(dtime), dataStyle)
            worksheet.write_formula(row, 2, "=SUM(D%s:F%s)/1000" % (row + 1, row + 1), dataStyle)
            worksheet.write_formula(row, 6,
                                    '=IF(C%s>3,"超时",IF(C%s=0,"超时",IF(C%s>3,"超时","OK")))' % (row + 1, row + 1, row + 1),
                                    dataStyle)
            row += 1

    workbook.close()


if __name__ == '__main__':
    main()
