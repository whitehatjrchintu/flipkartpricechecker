from apscheduler.schedulers.background import BackgroundScheduler
from webdriver_manager.chrome import ChromeDriverManager
from pyrogram import Client, filters, idle
import apscheduler.schedulers.blocking
from selenium import webdriver
from datetime import datetime
from os import environ
import requests
import logging
import pytz
import re
import os

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
info = "Greetings from Heroku."
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
print(info)

def job():
   msg = app.send_message(teri_chat_id_daal_bhsdk, "Doing.")
   gChromeOptions = webdriver.ChromeOptions()
   gChromeOptions.add_argument("window-size=1920x1480")
   gChromeOptions.add_argument("disable-dev-shm-usage")
   gDriver = webdriver.Chrome(chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install())
   gDriver.get('https://www.flipkart.com/redmi-k20-pro-glacier-blue-128-gb/p/itmfgfjthe3dyjp3')
   price = gDriver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
   x1 = price.text
   print(x1)
   IST = pytz.timezone('Asia/Kolkata')
   datetime_ist = datetime.now(IST)
   app.send_message(teri_chat_id_daal_bhsdk, "k20 pro's price at " + datetime_ist.strftime('%d:%m:%Y %H:%M:%S') + " is :- " + x1)
   msg.delete()
   gDriver.close()

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(job_defaults=job_defaults)
scheduler.add_job(job, "interval", seconds=1740)

scheduler.start()
app.run()
