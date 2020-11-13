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

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html

if __name__ == "__main__":
    search = input("请输入您想查询的内容（键入end退出）：")
    head = "https://www.youlai.cn/cse/search/?q="
    digit = np.arange(1,10)
    lianjie = "&page="

    while search != 'end':
        for i in range(len(digit)):
            path = head + search + lianjie + str(digit[i])
            b = get_html(path)
            html = lxml.html.fromstring(b)
            answers = html.xpath('//div[@class="se-p-line3-text"]//text()')
            if len(answers) == 0:
                continue
            else:
                result = answers[0]
                print(result)
        search = input('请输入您要搜索的内容（输入end退出）：')
    else:
        print('已经退出程序！')







