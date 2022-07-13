import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

import Additional
import Scraper

cont_1 = ''


class ComposeEmail:
    @staticmethod
    def sendmail():
        receiver_email = ''
        t = datetime.datetime.now()
        global cont_1
        cont_2 = Scraper.PerformScrape.extractor('https://news.ycombinator.com/')
        cont_1 += cont_2
        cont_1 += '<br>---------<br>'
        cont_1 += '<br><br>---End---'
        subject = "Top News from HackerNews" + " " + str(t.day) + "-" + str(t.month) + "-" + str(t.year)
        body = cont_1
        sender_email = input("Enter Your Email: ")
        choice = input("""
>send1 (To send to a single address)
>send2 (To send to multiple addresses)
>""")
        if choice == "send1":
            receiver_email = input("Enter the Receiver's Email: ")
        elif choice == "send2":
            n = int(input("Enter the number of emails: "))
            i = 0
            receiver_email = ''
            for i in range(n):
                r_mail = input(f'Email {(i+1)}: ')
                receiver_email += r_mail + ', '
        else:
            print("Invalid Input")
            Additional.act_2()
        password = input("Enter the password: ")

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        message.attach(MIMEText(body, "html"))
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.gmx.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        print("Email Sent")
        print("Again?")
