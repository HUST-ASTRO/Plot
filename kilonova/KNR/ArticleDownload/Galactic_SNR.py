# -*- coding: utf-8 -*-
# @Time    : 18-1-27 下午4:40
# @Author  : YuLiu
# @Email   : 335992260@qq.com
# @File    : Galactic_SNR.py
# @Software: PyCharm

import os
from urllib.request import urlopen
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

html = urlopen("http://www.mrao.cam.ac.uk/surveys/snrs/snrs.data.html")
bsObj = BeautifulSoup(html, "lxml")

coordinate = input("input Galactic coordinate (8.9  +0.4):")

TargetList = bsObj.findAll("a")
for Target in TargetList:
    if coordinate == Target.get_text():
        web = Target.attrs['href']

website = "http://www.mrao.cam.ac.uk/surveys/snrs/" + web
html = urlopen(website)
bsObj = BeautifulSoup(html, "lxml")

Title = bsObj.findAll("p", {"class": 'L'})[0]
path = "/home/hust/Desktop/ArticleDownload/" + str(Title.get_text())
isExists = os.path.exists(path)
if not isExists:
    os.makedirs(path)

ArticleList = bsObj.findAll("span", {"class": 'S'})
for Article in ArticleList:
    ADSwebsite = Article.a.attrs['href']
    html = urlopen(ADSwebsite)
    bsObj = BeautifulSoup(html, "lxml")
    file = bsObj.findAll("td", {"valign": 'top'})[1].get_text()
    UrlList = bsObj.findAll("a", {"class": 'oa'})
    for fileUrl in UrlList:
        if fileUrl.get_text() == 'Full Refereed Journal Article (PDF/Postscript)':
            savePath = path + '/' + file + '.pdf'
            if os.path.isfile(savePath):
                os.remove(savePath)  # 覆盖原文件
            urlretrieve(fileUrl.attrs['href'], savePath)
