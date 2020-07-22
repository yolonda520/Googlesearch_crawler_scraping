# %%
# smtplib is used for the mailing action of the mail
import smtplib
# email is used for building the content of the mail
from email.mime.text import MIMEText
# for building headers(Subject) of the mail
from email.header import Header
# Import CSV module for reading mailbox information
import csv
# %%
# Sender's information: Email address, Email authorization code/password
# email sender input own email address
from_addr = input('Please input your email address:')
# Your authorization code number, may not email passward
password = input('Please input your email password:')

# Recipient's multiple mailbox
# we can change list to str later: msg['To'] = Header(",".join(to_addr))  
to_addr = ['350499655@qq.com','yuhuang2018@student.hult.edu','yolonda520@gmail.com','huangyu870906@163.com']

# Sender server
smtp_server = 'smtp.gmail.com'

text = '''
Hi Ceme,
          
This is Yolonda. Put the text here can be sent email text with same fomat!
​Happy every day!
​          
Regards,
Yolonda
'''

# The first parameter is content, the second parameter is format (plain is plain text), and the third parameter is code
msg = MIMEText(text,'plain','utf-8')

# Header information
msg['From'] = Header(from_addr)
# msg['To'] = Header(to_addr) here need change list to str:
msg['To'] = Header(",".join(to_addr))  
msg['Subject'] = Header('Sorry,This is a python test')
# I can define 'from','to','Subject', for example:
# msg['From'] = Header('Yolonda H')
# msg['To'] = Header('Lover')
# msg['Subject'] = Header('This is a pyhton test')

# Enable the sending service, which USES encrypted transmission
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# Log in to your email address
# EDIT: Google blocks sign-in attempts from apps which do not use modern security standards. You can however, turn on/off this safety feature by going to the link below:
# Go to this link and select Turn On https://www.google.com/settings/security/lesssecureapps
server.login(from_addr, password)

try:
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('Congratuations, email successful sent!')
except:
    print('email failed send, try again.')

# 关闭服务器
server.quit()
 

# %%
