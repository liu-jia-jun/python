from openpyxl import Workbook
# 构建电子表格对象

wb= Workbook()
print(wb)
# 操作表
sheet = wb.active

print(sheet)

sheet.title ="学生信息表"

print(sheet.title)

# 在单元格中写内容
sheet["A1"]="序号"
sheet["B1"]="姓名"
print(sheet["A1"])
print(sheet["A1"].value)
# 保存excel文件
wb.save("student.xlsx")


