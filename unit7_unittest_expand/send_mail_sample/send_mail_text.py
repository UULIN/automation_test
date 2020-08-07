import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮件主题
subject = 'python email test'
# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
# 发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.126.com")
smtp.login("feng_er_lin@126.com","NHDSUDADYBYOEEYF")
smtp.sendmail("feng_er_lin@126.com","1036190402@qq.com", msg.as_string())
smtp.quit()