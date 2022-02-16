from asyncio import SendfileNotAvailableError
from cgitb import html
import email
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import environ, path
from dotenv import load_dotenv


sender_email = environ.get('SENDER_EMAIL')
reciever_email = environ.get('RECIEVER_EMAIL')

def send_email(name, user_email, message):
    port = 465 #for ssl
    password = environ.get('SENDER_EMAIL_PASSWORD')

    email_tosend = MIMEMultipart("alernative")
    email_tosend["Subject"] = "Message from "+name
    email_tosend["From"] = sender_email
    email_tosend["To"] = reciever_email

    #creating html for email
    html = """\
    <html>
        <body>
            <p>MDG,<br>
                you have a new message from {}:<br>
                {}
            </p>
        </body>
    </html>   
    """.format(user_email,message)
    email_tosend.attach(MIMEText(html, 'html'))
    #create secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email, reciever_email, email_tosend.as_string())
        
#figure out a way to include the message within the html