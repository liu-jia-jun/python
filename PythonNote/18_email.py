import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
import pandas as pd
#读取excel的数据
detail = pd.read_excel("data/工资单2.xlsx")
print(detail.values)
for i in detail.values:
    receiver = str(i[2])
    name=i[1]
    s =""
    print(receiver)
    for j in i:
        s+=str(j)+" "
        #print(j)
    print(s)
    msg = MIMEText(s,'plain','utf-8')
    msg["from"] = 'caolianglyf@126.com'
    msg["to"] = receiver
    msg['Subject'] = Header('工资单', 'utf-8')
    sender = 'caolianglyf@126.com'
    user = 'caolianglyf@126.com'
    password = 'RIBMXNGSEDTWVSHM'
    smtpserver = 'smtp.126.com'
    smtp = smtplib.SMTP() #实例化SMTP对象
    smtp.connect(smtpserver,25) #（缺省）默认端口是25 也可以根据服务器进行设定
    smtp.login(user,password) #登陆smtp服务器
    smtp.sendmail(sender,receiver,msg.as_string()) #发送邮件 ，这里有三个参数
    smtp.quit()
#自动发邮件