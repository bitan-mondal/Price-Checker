import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('<EMAIL>','<PASSWORD>')

    subject = 'Price Drop Alert!'
    body = 'Check the Amazon link '+URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '<EMAIL-FROM>',
        '<EMAIL-TO>',
         msg
    )

    #print('Email has been sent!')

    server.quit()

def check_price(URL,headers):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = (price[2:7])

    if(converted_price < desiredPrice):
        send_email()

    print(title.strip())
    print(converted_price)

    
if __name__ == "__main__":
    URL = 'https://www.amazon.in/Adidas-Furio-Running-Shoes-8-CJ0110/dp/B07B2J4V8C/ref=sr_1_35?keywords=adidas+shoes&qid=1566905021&s=gateway&sr=8-35'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    timeInSecondsToWait = 3600
    desiredPrice = "2,250"
    while(True):
        check_price(URL,headers,desiredPrice)
        time.sleep(timeInSecondsToWait)
