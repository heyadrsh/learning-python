from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Me"
message["to"] = "test@test.com"
message["subject"] = "Python Email Test"

message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("python.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test@gmail.com", "password")
    smtp.send_message(message)
    print("Sent...") 