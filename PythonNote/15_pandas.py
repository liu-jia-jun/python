
# 对于pandas库的讲解
import pandas as pd
from sqlalchemy import create_engine
conn = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8")
detail = pd.read_sql("meal_order_detail1",con=conn)
#打印表的字段名
print(detail.columns)
#对detail做查改增删
print(detail['dishes_name'])
print(detail[['order_id','dishes_name']])
#使用head() tail()
print(detail.head())
print(detail.tail())
#loc方法访问数据
data = detail.loc[4,'dishes_name']
print(data)
#按条件查看
data2 = detail.loc[detail['order_id']=='417',['order_id','dishes_name']]
print(data2)
#改数据
detail.loc[detail['order_id']=='417','order_id']='417000'
print("修改后再查")
data2 = detail.loc[detail['order_id']=='417',['order_id','dishes_name']]
print(data2)
data2 = detail.loc[detail['order_id']=='417000',['order_id','dishes_name']]
print(data2)
print(detail.columns)
#增加数据
detail['pay_way']='现金支付'
print(detail.loc[0:4,'pay_way'])
print(detail.columns)
detail['payment']=detail['counts']*detail['amounts']
print(detail.loc[2775:,['counts','amounts','payment']])