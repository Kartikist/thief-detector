
import smtplib
import os
import imghdr
from email.message import EmailMessage

username = 'neti.kartik@gmail.com'
password = os.getenv('PASSWORD')
receiver = 'neti.kartik@gmail.com'

def send_email(img_path):
    
    email_message = EmailMessage()
    email_message["Subject"] = "An object showed up"
    email_message.set_content("Just found a new object")
    
    with open(img_path, 'rb') as file:
        content = file.read()
        
    email_message.add_attachment(content, maintype = "image", subtype=imghdr.what(None, content) )
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver,email_message.as_string())
    gmail.quit


   