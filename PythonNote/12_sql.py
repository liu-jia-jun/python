

#引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors


#获取数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='pythondb',
                             charset='utf8mb4')
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 插入语句
        # 创建SQL语句
        sql = "insert into `urls`(`urlname`,`urlhref`) values('百度','https://www.baidu.com')"
        # 执行SQL语句
        cursor.execute(sql)
        #提交
        connection.commit()
        #查询语句
        sql = "select `urlname`,`urlhref` from `urls` where `id` is not null"
        #查询所有行数
        count = cursor.execute(sql)
        print(count)
        #查询前三条数据
        result = cursor.fetchmany(size=3)
        print(result)
finally:
    connection.close()


