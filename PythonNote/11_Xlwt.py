# xlwt 将数据存储到excel表中

import xlwt
'''
# 保存数据到excel表的基本操作
workbook = xlwt.Workbook(encoding = "utf-8") # 创建workbook 对象即类似于文件对象
worksheet = workbook.add_sheet("sheet1") # 创建工作表
worksheet.write(0,0,"hello") # 写入数据，worksheet.write(第几行，第几列，写入的内容)
workbook.save("temp.xls") # 保存数据表
'''


workbook = xlwt.Workbook(encoding = "utf-8") # 创建workbook 对象即类似于文件对象
worksheet = workbook.add_sheet("sheet1") # 创建工作表

for i in range(1,10):
    for j in range(1,i+1):
        worksheet.write(i-1,j-1,str(i)+"*"+str(j)+"="+str(i*j))


workbook.save("temp.xls") # 保存数据表