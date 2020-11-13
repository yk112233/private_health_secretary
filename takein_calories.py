#饮食话语输入格式：300克汉堡。
import xlrd
import re
import math
import numpy as np

def read_excel(path):
    # 打开excel表，填写路径
    book = xlrd.open_workbook(path)
    # 找到sheet页
    table = book.sheet_by_name("food_categories")
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

def food_calories_calculate(yuyan):
    path = "D:\\数学建模\\hackathon\\food_category.xls"
    d = read_excel(path)
    p = r'([0-9]+)'
    pattern = re.compile(p)
    digit = pattern.search(yuyan).group()

    pattern1 = re.compile("毫升|克|\d+|。")
    name = re.sub(pattern1, "", yuyan)

    category = d[name]
    # path_data = "D:\\数学建模\\hackathon\\food_data\group" + str(category) + ".xls"
    # df = pd.read_excel(path_data, usecols=[0],
    #                    names=None)  # 读取项目名称列,不要列名
    print(category)
    path_data = "D:\\数学建模\\hackathon\\food_data\group" + str(category) + ".xls"
    book = xlrd.open_workbook(path_data)
    sheet = book.sheet_by_name("My Worksheet")
    s = []
    for i in range(sheet.nrows):
        s.append(re.sub("/ ", "", sheet.cell(i, 1).value))
    print(s)
    index = s.index(name)
    calory_data = float(sheet.cell(index, 2).value)/100*float(digit)
    sugar_data = float(sheet.cell(index, 3).value)/100*float(digit)
    fat_data = float(sheet.cell(index, 4).value)/100*float(digit)
    protein_data = float(sheet.cell(index, 5).value)/100*float(digit)
    fiber_data = float(sheet.cell(index, 6).value)/100*float(digit)
    print("摄入：")
    print("卡路里：", calory_data, "大卡")
    print("碳水化合物：", sugar_data, "克")
    print("脂肪：", fat_data, "克")
    print("蛋白质：", protein_data, "克")
    print("纤维素：", fiber_data, "克")

    return calory_data, sugar_data, fat_data, protein_data, fiber_data

food_calories_calculate("200毫升可乐")



