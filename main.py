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
    baseUrl = "https://movie.douban.com/top250"
    # 得到并处理数据
    dataList = getData(baseUrl)
    # 保存数据
    savePath = "./豆瓣电影Top250.xls"
    saveData(savePath)

def saveData(savePath):
    print("saveData")




def getData(baseUrl):
    dataList = []

    return dataList

# 表明函数入口，清晰代码走向
if __name__ == '__main__':
    main()
