import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

sender_email = "refridgeratorsensor@gmail.com"
password = "cs370termproject"
sendto_email = "britnall@colostate.edu"


def send_temp_gmail_alert(temp, time):
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "CRITICAL Refrigerator Temperature!"
    msg['From'] = "Raspberry Pi"
    msg['To'] = sendto_email
    
    time_str = "{:%A %m/%d/%Y %I:%M %p}".format(time)
    html = """\
        <html>
        <head>
        <font size="6">
        <h1><strong>Critical Warning!</strong><br>
        </font>
        <font size="4">
        <i>{}</i><br></h1>
        </font>
        </head>
        <body>
        <p>
        <font size="5">
        The temperature of your fridge is at {}{}F.<br>
        <b>Please remove all food from your fridge before contamination.</b><br>
        </font>
        </p>
        </body>
        </html>
        """.format(time_str, temp, chr(176))
    
    body = MIMEText(html, 'html')
    msg.attach(body)

    print("send email")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, sendto_email, msg.as_string())
    server.close()


def send_pic_gmail_alert(image_data, image_name, time):
    msg = MIMEMultipart("alternative")
    msg['Subject'] = 'SOMEONE IS IN YOUR FRIDGE'
    msg['From'] = 'Raspberry Pi'
    msg['To'] = sendto_email

    time_str = "{:%A %m/%d/%Y %I:%M %p}".format(time)
    html = """\
        <html>
        <head>
        <font size="6">
        <h1><strong>Someone is in your fridge!</strong><br>
        </font>
        <font size="4">
        <i>{}</i><br></h1>
        </font>
        </head>
        <body>
        <p>
        <font size="5">
        Here is what your fridge looks like.<br>
        </font>
        </p>
        </body>
        </html>
        """.format(time_str)

    text = MIMEText(html, 'html')
    msg.attach(text)
    image = MIMEImage(image_data, name=os.path.basename(image_name))
    msg.attach(image)

    print("send email")
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(sender_email, password)
    s.sendmail(sender_email, sendto_email, msg.as_string())
    s.close()


if __name__ == '__main__':
    import datetime
    send_temp_gmail_alert(98, datetime.datetime.now())
