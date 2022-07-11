import requests
from bs4 import BeautifulSoup
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import datetime

t = datetime.datetime.now()
cont_1 = ''


def extractor(url):
    print("Extracting news...")
    cont_2 = ''
    cont_2 += ('<h1>Hacker News Top Stories:</h1>\n'+'<h1>'+'-'*50+'<br>')
    res = requests.get(url)
    cont_1 = res.content
    soup = BeautifulSoup(cont_1, 'html.parser')
    # 'td' is table element. Attributes --> class, title, valign(Empty)
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        # enumeration provides index and the actual tag of the extracted page
        cont_2 += ((str(i+1)+' :: '+ '<a=href"' +tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text != 'More' else '')
    return(cont_2)


def help():
    print("Refer to the Readme.md")
    exit()


def yes():
    os.system("shutdown /s /t 1")


print("""
        -----------------------------------
        |                                 |
        |   MAIL HACKERNEWS TOP STORIES   |
        |                                 |
        -----------------------------------
""")

user_input_1 = input("""
        ------------------------------------
        |   Type:                          |
        |     "send" to proceed            |
        |     "quit" to exit               |
        |     "help" to reboot             |
        |     "meh" to get :D              |
        ------------------------------------

>""")

def drama():
    if user_input_1=="send":
        return
    elif user_input_1=="quit":
        exit()
    elif user_input_1=="help":
        help()
    elif user_input_1=="meh":
        yes()
    else:
        print("Invalid Input. Type help or quit the program")

drama()
cont_2 = extractor('https://news.ycombinator.com/')
cont_1 += cont_2
cont_1 += '<br>---------<br>'
cont_1 += '<br><br>---End---'

print("Composing Email")

subject = "Top News from HackerNews"+" "+str(t.day)+"-"+str(t.month)+"-"+str(t.year)

body = cont_1
sender_email = input("Enter the Sender Email: ")
# TODO: Handling multiple emails
receiver_email = input("Enter the Receiver Email: ")
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
# TODO: User input for another attempt
