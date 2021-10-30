# 词云的制作

import jieba  as jb# 用于分词
from matplotlib import pyplot as plt  # 用于绘图，数据可视化
from wordcloud import WordCloud # 词云

from PIL import Image # 图片处理
import numpy as np # 矩阵计算
import pymysql.cursors

#获取数据库连接
# 从数据库中获取多需要的文字
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='pythondb',
                             charset='utf8mb4')


try:
    # 获取会话指针
    with connection.cursor() as cursor:
        #查询语句
        sql = "select instroduction from movie"
        #查询所有行数
        count = cursor.execute(sql)
        print(count)
        #查询前三条数据
        result = cursor.fetchmany(size=count)
        print(result)
finally:
    connection.close()

text = ""
# 字符串拼接，拼接成一个字符串用于分词
for i in range(len(result)):
    text += str(result[i])


# 分词
cut = jb.cut(text)
string = ' '.join(cut)
print(len(string))
print(string)

img = Image.open(r'./imgs/img1.png') # 打开遮罩图片
img_array = np.array(img) # 将图片转换成数组

wc = WordCloud(
    background_color = "white", # 生成的词云图片的主题颜色
    mask = img_array,
    font_path = "simsun.ttc" # 设置字体，字体在电脑位置 ：C:\Windows\Fonts   选中字体，右击属性，复制text框中的内容即可
)
wc.generate_from_text(string)


# 绘制图片
fig = plt.figure(1)

plt.imshow(wc)
plt.axis("off") # 是否显示坐标

plt.show() # 显示生成的词云图片

# 输出词云图片文件
plt.savefig(r'./imgs/wordcloud.jpg',dpi=500) # 路径和分辨率