#
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
conn = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8")
detail = pd.read_sql("meal_order_detail1",con=conn)
print(detail.columns)
#对其中某几列的数据做分组  分组对象 detailGroup
detailGroup = detail[['order_id','counts', 'amounts']].groupby(by = "order_id")
print(detailGroup)

# 聚合就是汇总，agg方法
# 汇总：求和，求平均数，求最大最小，求标准差，方差等
print(detail[["counts","amounts"]].agg(np.mean))

# 以字典类型的数据作为参数，汇总
print(detail.agg({"counts":np.sum,"amounts":np.mean}))
print(detail.agg({"counts":np.sum,"amounts":[np.sum,np.mean]}))

def doubleSum(data):
    return data.sum()*2

print(detail.agg({"amounts":doubleSum}))

# 分组聚合 对分组使用汇总函数
# 对以订单号分组的销售量和金额做求和汇总
print(detailGroup.agg(np.sum).head())

print(detail['order_id'].head(20))