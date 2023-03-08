from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

email_sender = ''
# put your gmail app password in a .env file with the key APP_PASSWORD
email_password = os.getenv('APP_PASSWORD')

email_receiver = input("Recipient's Address: ")
email_subject = input("Email Subject: ")
email_body = ''
print("Email body (press enter on empty line when finished):")

while True:
    text = input('''''') + '\n'

    if text == '\n':
        break

    email_body += text

message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = email_subject
message.set_content(email_body)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, message.as_string())

    print("Email sent.")

    smtp.quit()
