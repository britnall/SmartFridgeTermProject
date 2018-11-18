import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "refridgeratorsensor@gmail.com"
password = "cs370termproject"
sendto_email = "britnall@colostate.edu"


def send_gmail_alert(temp, time):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)

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

    server.sendmail(sender_email, sendto_email, msg.as_string())
    server.quit()


if __name__ == '__main__':
    import datetime
    send_gmail_alert(98, datetime.datetime.now())
