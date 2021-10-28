'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

'''

from bs4 import BeautifulSoup # 从bs4这个包中引入BeautifulSoup模块  用于网页解析，获取数据

import re # 正则表达式，进行文字匹配

import urllib.request,urllib.error  # 指定URL 用于获取网页数据

import xlwt # 进行excel 操作

import sqlite3 # 进行SQLite 数据库操作

# 程序主方法
def main():
    # 爬取网页
    baseUrl = "https://movie.douban.com/top250?start="
    # 得到并处理数据
    dataList = getData(baseUrl)
    # 保存数据
    savePath = "./豆瓣电影Top250.xls"
    saveData(savePath)



def saveData(savePath):
    print("saveData")




def getData(baseUrl):
    dataList = []

    for i in range(0,10):

        html = askURL(baseUrl+str(i*25))

    return dataList

# 得到指定一个URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息，防止服务器识别出该程序为爬虫而限制访问
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件）
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


# 表明函数入口，清晰代码走向
if __name__ == '__main__':
    main()
