import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mails(complete_data):
    for data in complete_data:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        username = "sairutwika1408@gmail.com"
        password = "lkte omxr usrc jmcn"

        from_email = "sairutwika1408@gmail.com"
        to_email = data[1]
        subject = "Fee Update"
        body = f"Dear {data[0]},\n we are from akshaya school  You have No Fee Pending\nThank You !"

        msg = MIMEMultipart()
        msg['From'] = from_email    
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(username,password)
        server.send_message(msg)
        server.quit()
        print(f"Mail sent to {data[0]}")


