# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Email(object):
	def __init__(self):
		# 第三方 SMTP 服务
		
		
	def sendmail(self,subject,content,receivers):
		message = MIMEText(content, 'plain', 'utf-8')
		message['Subject'] = Header(subject, 'utf-8')
		message['From'] = Header("Fortune", 'utf-8')
		server = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
		server.set_debuglevel(1)
		server.login(self.mail_user,self.mail_pass)  
		server.sendmail(self.sender, receivers, message.as_string())
