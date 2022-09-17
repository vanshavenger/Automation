import requests # http requests

from bs4 import BeautifulSoup # web scraping
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''


def extract_news(url):
    print('Extracting News Stories...')
    cnt = ''
    cnt +=('<b>Google Top News:</b>\n'+'<br>'+'-'*50+'<br><br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('article',attrs={'class':'MQsxIb'})):
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
    return(cnt)
    
cnt = extract_news('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
content += cnt
content += ('<br>------------------------<br>')
content += ('<br><br>End of Automated Message')


print('Composing Email...')

# update your email details
#Use App Passwords

SERVER = 'smtp.gmail.com' # "your smtp server"
PORT = 587 # your port number
FROM = '******************@gmail.com' # "your from email id"
TO = '******************@gmail.com' # "your to email ids"  # can be a list
PASS = '******************' # "your email id's password"

msg = MIMEMultipart() #email body

msg['Subject'] = 'Top Google News [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html')) #so that the text is in HTML form

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1) #to see debug messages if the server has issue in connecting if the server has any problem, if you want to see error messages the put it in 1 otherwise 0
server.ehlo() # used to initiate the server
server.starttls() #start tls connection which is a secure connection
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()





