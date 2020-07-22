# When you send group email using his template, the receivers email addresses are hidden when they receive email.
 # %%
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = input('Please input your email:')
#    msg['To'] = Header(",".join(to_addr)) ''' 
receiver_email = ",".join(['yuhuang2018@student.hult.edu','yolonda520@gmail.com','huangyu870906@163.com','350499655@qq.com'])
password = input("Type your password and press enter:")
message = """\
Subject: This is title
Hi,
This is a test!
This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    try:
        server.sendmail(sender_email, receiver_email, message)
        print('Congratuations, email successful sent!')
    except:
        print('email failed send, try again.')
    

# %%
