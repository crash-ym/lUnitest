#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import time
import logging

sender = 'yangm1022@163.com'
mypass = 'ym2014014362'
receivers = 'yangming@bw30.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱



def mail(filename):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    rel = True
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        #message['From'] = Header("LUnitest 测试邮件", 'utf-8')
        message['From'] = formataddr(["yangm1022", sender])
        #message['To'] = Header("测试报告", 'utf-8')
        message['To'] = formataddr(["yangming", receivers])
        subject = 'LUnitest 测试报告'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('测试报告', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字

        #时间命名文件
        now = int(time.time())
        now = str(now)
        strname = 'TReport' + now + '.html'
        att1["Content-Disposition"] = 'attachment; filename='+strname
        message.attach(att1)

        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, mypass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receivers, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        #print("已执行")
        logger.info("执行成功")
        return rel
    except Exception:
        rel =False
        #print("执行异常")
        logger.error("执行失败")
        return rel


if __name__ == '__main__':
    mail()