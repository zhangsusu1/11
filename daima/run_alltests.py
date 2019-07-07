import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP
#from tensorflow.examples.tutorials.mnist import input_data
import smtplib
import io
import sys
#def createsuite():
def createsuite():
    #mnist = input_data.read_data_sets("D:\document\daima\MNIST_data/", one_hot=True)
    test_dir="D:\\document\\daima\\test_case"
    discov=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    suite=unittest.TestSuite()
    for test_case in discov:
        suite.addTest(test_case)
    return suite
now=time.strftime("%Y-%m-%d %H-%M-%S")
reportname=".\\report\\"+now+"result.html"
file1=open(reportname,'wb')
runner=HTMLTestRunner(stream=file1,title='pandatv',description='test_case')

def sendReport(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=Header('手机自动化测试报告','utf-8')
    msg['From']='zj837028840@163.com'
    msg['To']='zhangss_1992@163.com'
    smtp=smtplib.SMTP_SSL('smtp.163.com',465)
    #smtp.connect('smtp.163.com')
    #smtp=smtplib.SMTP('smtp.126.com')
    smtp.login("zj837028840@163.com","zj1025ycr1214")
    smtp.sendmail(from_addr="zj837028840@163.com",to_addrs="zhangss_1992@163.com",msg=msg.as_string())
    smtp.quit()
    print('测试报告发送成功')
altestnames=createsuite()
runner.run(altestnames)
file1.close()
sendReport(reportname)
