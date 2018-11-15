# -*- coding:utf-8-*-

import xlsxwriter

from collect.collector import *

reload(sys)
sys.setdefaultencoding('utf-8')


def workcharts(workbook, worksheet, sheetnames, seriesnames, col, position):
    chart1 = workbook.add_chart({"type": "bar"})
    chart1.add_series({
        "name": "%s" % (seriesnames),
        "categories": "='%s'!$B$3:$B$8" % sheetnames,
        "values": "'%s'!$%s$3:$%s$8" % (sheetnames, col, col),
        "data_labels": {"value": True},
        "line": {"none": True},
    })

    chart1.set_title({"name": "%s的%s" % (sheetnames, seriesnames)})

    chart1.set_style(27)
    worksheet.insert_chart(position, chart1)


def diaoyong():
    heads = ["国家/地区", "访问总时间(s)"]
    data = [
        ["China-Hong Kong(香港)", "Germany-Munich(德国-慕尼黑)", "Sweden-Stockholm(瑞典-斯德哥尔摩)", "United Kingdom-London(英国-伦敦)",
         "Italy-Padova(意大利-帕多瓦)", "Switzerland-Zurich(瑞士-苏黎世)"],
        [1.763, 1.125, 1.103, 1.318, 0, 1.049],
    ]
    workbook = xlsxwriter.Workbook(u"测试数据.xlsx")
    style = workbook.add_format({"bold": 1, "align": "center", "bg_color": "#808080"})

    worksheet = workbook.add_worksheet("数据分析图标汇总")
    worksheet.write_row("B2", heads, style)
    worksheet.write_column("B3", data[0])
    worksheet.write_column("C3", data[1])

    workchart = workbook.add_worksheet("测试数据")
    sites = {
        "www.platon.network": "Platon(京东)"
    }
    for site in sites.keys():
        workcharts(workbook, workchart, worksheet.name, "访问时间", "C", "B10")
        workcharts(workbook, workchart, worksheet.name, "访问时间", "C", "B26")
    workbook.close()


diaoyong()

# def workcharts(workbook, worksheet, sheetnames, seriesnames, col, position)
