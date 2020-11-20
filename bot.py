from apscheduler.schedulers.background import BackgroundScheduler
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from datetime import datetime
from pyrogram import Client
from os import environ
import smtplib
import pytz

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
info = "Greetings from Heroku."
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
print(info)

def job():
   msg = app.send_message(teri_chat_id_daal, "Doing.")
   gChromeOptions = webdriver.ChromeOptions()
   gChromeOptions.add_argument("window-size=1920x1480")
   gChromeOptions.add_argument("disable-dev-shm-usage")
   gDriver = webdriver.Chrome(chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install())
   gDriver.get('https://www.flipkart.com/redmi-k20-pro-glacier-blue-128-gb/p/itmfgfjthe3dyjp3')
   pricee = gDriver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
   x1 = pricee.text
   print(x1)
   price = x1.lstrip("₹")
   print(price)
   IST = pytz.timezone('Asia/Kolkata')
   datetime_ist = datetime.now(IST)
   app.send_message(teri_chat_id_daal, "k20 pro's price at " + datetime_ist.strftime('%d:%m:%Y %H:%M:%S') + " is :- " + x1)
   msg.delete()
   gDriver.close()

   my_price = "25,000"
   if price <= my_price:
      print("price kam ho gya.")
      s = smtplib.SMTP('smtp.gmail.com', 587)
      s.ehlo()
      s.starttls()
      s.ehlo()
      s.login("sender_email_id", "sender_email_id_password")
      subject = "price kam ho gya"
      body = "price kam ho gya k20 pro ka. Jaldi kar:- https://www.flipkart.com/redmi-k20-pro-glacier-blue-128-gb/p/itmfgfjthe3dyjp3"
      message = f"Subject: {subject}\n\n{body}"
      s.sendmail("sender_email_id", "receiver_email_id", message)
      print("Email has been sent.")
      s.quit()
   else:
      pass
   
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(job_defaults=job_defaults)
scheduler.add_job(job, "interval", seconds=1740)

scheduler.start()
app.run()
