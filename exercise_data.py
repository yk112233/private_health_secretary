import xlrd
import re
import math
import numpy as np

def read_excel(path):
    # 打开excel表，填写路径
    book = xlrd.open_workbook(path)
    # 找到sheet页
    table = book.sheet_by_name("Sheet1")
    # 获取总行数总列数
    row_Num = table.nrows
    col_Num = table.ncols

    if row_Num <= 1:
        print("没数据")
    else:
        d = dict()
        for i in range(row_Num):
            d[re.sub("/ ", "", table.cell(i, 0).value)] = table.cell(i, 1).value

    return d



def exercise_calculate(yuyan):
    # 种类 + digit + 单位
    path = "D:\数学建模\hackathon\exercise_xiaohao.xlsx"
    d = read_excel(path)
    p = r'([0-9]+)'
    pattern = re.compile(p)
    digit = pattern.search(yuyan).group()

    pattern1 = re.compile("分钟|\d+|。")
    name = re.sub(pattern1, "", yuyan)

    unit = d[name]

    result = float(digit)*unit/60

    print(result, "千卡")

    return result

exercise_calculate("走路10分钟。")



