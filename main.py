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

    for items in dataList:
        for item in items:
            print(item)

    # 保存数据
    savePath = "./豆瓣电影Top250.xls"
    saveData(savePath)



# 定义全局变量，匹配规则，用于查找想要的内容
# 定义影片链接规则
findLink = re.compile(r'<a href="(.*?)">') # 创建正则表达式对象，表示规则（字符串的匹配模式）
# 定义图片路径规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) # re.S 让换行符包含在字符串中
# 定义影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)






def saveData(savePath):
    print("saveData")




def getData(baseUrl):
    dataList = []

    for i in range(0,1):
        # 得到数据
        html = askURL(baseUrl+str(i*25))
        # 逐一解析得到的数据

        soup = BeautifulSoup(html,"html.parser")

        for item in soup.find_all('div',class_="item",limit=2):
            # data 列表用于保存一部电影的全部信息
            data = []
            item = str(item)
#             print(item)

            link = re.findall(findLink,item)[0] # re库用来通过正则表达式查找指定的字符串
            data.append(link) # 添加链接
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc) # 添加图片地址
            titles = re.findall(findTitle,item) # 影片名可能有两种情况，分情况将影片名进行存储
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle) # 添加中文名
                otitle = titles[1].replace("/","") # 将外国影片名中的/ 替换掉
                data.append(otitle) # 添加外国名
            else:
                data.append(titles[0])
                data.append("") # 当影片没有外国名是，使用空白字符给外国名占位

            rating = re.findall(findRating,item)[0]
            data.append(rating) # 添加评分
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum) # 添加评价人数

            inq = re.findall(findInq,item)
            if(len(inq)!= 0):
                inq = inq[0].replace("。","") # 去掉句号
                data.append(inq) # 添加概述
            else:
                data.append(" ") # 如果电影没有概述时，留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?"," ",bd) # 去掉<br/>
            bd = re.sub("/"," ",bd) # 去掉 /
            data.append(bd.strip()) # 去掉前后空格

            dataList.append(data) # 把解析好的电影的数据存放到dataList中，并返回



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
#         print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


# 表明函数入口，清晰代码走向
if __name__ == '__main__':
    main()
