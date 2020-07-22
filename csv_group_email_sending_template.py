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
# May your authorization code number, may not email passward, depends email domain
password = input('Please input your email password:')

# Sender server, here is gmail sample
smtp_server = 'smtp.gmail.com'

text = '''Hi Ceme,
          
This is Yolonda. Put the text here can be sent email text with same fomat!
​Happy every day!
​          
Regards,
Yolonda
'''
# %%
email_csv = 'SF_research_list.csv'
with open(email_csv, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for line in reader:
        to_addr = line[1]
        if to_addr == None or to_addr == '':
            continue
        print(to_addr)
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
        server.login(from_addr, password)
        try:
            server.sendmail(from_addr, to_addr, msg.as_string())
            print('Congratuations, email successful sent!')
        except:
            print('email failed send, try again.')
       
# Close server      
server.quit()

