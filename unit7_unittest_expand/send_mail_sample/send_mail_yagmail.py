import yagmail
# 连接邮件服务器
yag = yagmail.SMTP(user="feng_er_lin@126.com",password="NHDSUDADYBYOEEYF", host="smtp.126.com")

# 邮件正文
contents =['this is the body, i am xuyulin']

yag.send('feng_er_lin@126.com','subject',contents)