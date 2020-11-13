# -*- coding: utf-8 -*-
import re
import numpy as np
import requests
import lxml.html
import xlwt
import jieba
import jieba.posseg as psg
import os
from selenium import webdriver
import math

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html

if __name__ == "__main__":
    parent = "http://www.boohee.com"
    head = 'http://www.boohee.com/food/view_group/'
    groups = np.arange(1, 132)
    pages = ["", "?page=2", "?page=3", "?page=4", "?page=5", "?page=6", "?page=7", "?page=8", "?page=9", "?page=10"]

    # edgedriver = r"D:\python\Lib\site-packages\selenium\webdriver\edge\edgedriver_win32\msedgedriver.exe"
    # # 设置浏览器
    # os.environ["webdriver.edge.driver"] = edgedriver
    # browser = webdriver.Edge(edgedriver)
    # browser.minimize_window()
    workbook_FOOD = xlwt.Workbook(encoding='utf-8')
    worksheet_FOOD = workbook_FOOD.add_sheet('food_categories')
    count = 0

    for i in range(len(groups)):
        yk_cnt = 0
        units = []
        names = []
        calories = []
        fats = []
        fibers = []
        sugars = []
        proteins = []
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('My Worksheet')
        path1 = head + str(groups[i])
        bb = get_html(path1)
        html = lxml.html.fromstring(bb)
        jilu_raw = html.xpath('//div[@class="widget-pagination"]/span[@class="pagination-sum"]//text()')
        pattern = re.compile('\xa0(.+)\xa0')  # 匹配ab与ef之间的内容
        result = pattern.findall(jilu_raw[0])
        result = int(result[0])

        for j in range(math.ceil(result/10)):
            path2 = path1 + pages[j]
            reg = r'(/shiwu/[a-z,0-9,_,A-Z,-]+)'  # 正则表达式
            reg_ques = re.compile(reg)  # 编译一下正则表达式，运行的更快
            children_urls = reg_ques.findall(get_html(path2))  # 匹配正则表达式
            chidren_urls = list(set(children_urls))
            for k in range(len(chidren_urls)):
                pattern = re.compile("^\s+|\s+$|\n")
                pattern_unit = re.compile("含量|\(|每|100|\)")
                path3 = parent + chidren_urls[k]
                b = get_html(path3)
                html = lxml.html.fromstring(b)
                food_name_raw = html.xpath('//div[@class="widget-group-content container"]/h2[@class="crumb"]//text()')
                print(food_name_raw)
                print(path3)
                food_name = re.sub(pattern, "", food_name_raw[3])
                worksheet_FOOD.write(count, 0, food_name)
                worksheet_FOOD.write(count, 1, str(groups[i]))
                count += 1
                calories_raw = html.xpath('//div[@class="nutr-tag margin10"]/div/dl[2]/dd[1]//text()')
                calory = calories_raw[1]
                if calory == "一":
                    calory = 0

                sugars_raw = html.xpath('//div[@class="nutr-tag margin10"]/div/dl[2]/dd[2]//text()')
                sugar = sugars_raw[1]
                if sugar == "一":
                    sugar = 0

                fats_raw = html.xpath('//div[@class="nutr-tag margin10"]/div/dl[3]/dd[1]//text()')
                fat = fats_raw[1]
                if fat == "一":
                    fat = 0

                protein_raw = html.xpath('//div[@class="nutr-tag margin10"]/div/dl[3]/dd[2]//text()')
                protein = protein_raw[1]
                if protein == "一":
                    protein = 0

                fiber_raw = html.xpath('//div[@class="nutr-tag margin10"]/div/dl[4]/dd[1]//text()')
                fiber = fiber_raw[1]
                if fiber == "一":
                    fiber = 0

                unit_raw = html.xpath('//div[@class="nutr-tag margin10"]/div/dl[1]//text()')
                unit = re.sub(pattern_unit, "", unit_raw[-2])

                units.append(unit)
                names.append(food_name)
                calories.append(calory)
                sugars.append(sugar)
                fats.append(fat)
                proteins.append(protein)
                fibers.append(fiber)
            for m in range(len(names) - yk_cnt):
                # 写入excel
                # 参数对应 行, 列, 值
                worksheet.write(yk_cnt, 0, str(yk_cnt))
                worksheet.write(yk_cnt, 1, str(names[yk_cnt]))
                worksheet.write(yk_cnt, 2, str(calories[yk_cnt]))
                worksheet.write(yk_cnt, 3, str(sugars[yk_cnt]))
                worksheet.write(yk_cnt, 4, str(fats[yk_cnt]))
                worksheet.write(yk_cnt, 5, str(proteins[yk_cnt]))
                worksheet.write(yk_cnt, 6, str(fibers[yk_cnt]))
                worksheet.write(yk_cnt, 7, str(units[yk_cnt]))
                yk_cnt += 1
                print(yk_cnt)
                # 保存
        excel_name = "group" + str(groups[i]) + ".xls"
        workbook.save(excel_name)
    workbook_FOOD.save("food_category.xls")






