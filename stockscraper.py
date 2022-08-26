
#Webscraper for stocks with yahoo.com 

import requests #to access url
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' }

def check_price():

    page = requests.get(URL,headers=headers)
    soup=BeautifulSoup (page.content, 'html.parser')

    #print(soup.prettify())

    for apple in soup.find_all("div", {"class": "D(ib) Mt(-5px) Maw(38%)--tab768 Maw(38%) Mend(10px) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)"}):

        print (apple.get_text())

    for price in soup.find_all("div",{ "class":"D(ib) Mend(20px)"}):

        print (price.get_text())

    ActualPrice = (price.get_text())[0:3] #error taking price
    print("This is Actual Price: ", ActualPrice)

    if (int(ActualPrice)<170):
        send_mail()

    #print(ActualPrice)

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mr5501744@gmail.com','xojsgrowndkhdynt')
    subject =('Price for apple stock reduced')
    body ='Check yahoo link: https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mr5501744@gmail.com',
        'mar2002raj@gmail.com',
        msg
    )

    print('Email has been sent')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)


