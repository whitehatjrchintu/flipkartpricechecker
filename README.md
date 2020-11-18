# Flipkart price checker/monitoring telegram bot.

With this telegram bot you can monitor price of any Flipkart product. This TG bot is **heroku** based. Now before you continue i recommend you to read [**Note**](https://github.com/whitehatjrchintu/flipkartpricechecker/blob/main/README.md#note-) section.

## Prerequisites:-

1. Create account on [GitHub](https://www.github.com) (if you haven't).
2. Create account on [Heroku](https://dashboard.heroku.com) (if you haven't).
3. Create account on [Telegram](https://web.telegram.org) (if you haven't).
4. Go to [my.telegram.org/auth](https://my.telegram.org/auth), login and create app. Check [how to create app on telegram](https://core.telegram.org/api/obtaining_api_id). Now save api_id and api_hash which you got from [my.telegram.org/auth](https://my.telegram.org/auth).
5. Create a telegram bot by using [Bot Father](https://t.me/botfather). Check [how to create bot in telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot). [Bot Father](https://t.me/botfather) will give you bot token save that token.
6. So now you have saved **three** things:-
- api_id
- api_hash
- bot_token

## How to use?
### Step 1:
- Just git clone this repository and start working by editing the code
   ```shell
   git clone https://github.com/whitehatjrchintu/flipkartpricechecker.git
   cd flipkartpricechecker
- Or download this [repository](https://github.com/whitehatjrchintu/flipkartpricechecker/archive/main.zip) as zip.
  
### Step 2:
- After cd or unzip you have to edit **bot.py** file.

- In bot.py **teri_chat_id_daal** this mentioned two times. You have to replace this with your chat id. Search **@chatid_echo_bot** in telegram (This bot is not mine. You can google how to get chat id in telegram.) and click start this will give you your chat id. Now replace **teri_chat_id_daal** with your chat id number.

### Step 3:
- Now create repository (you can create private repository too.) in your github account and upload all 5 files.

### Step 4:
- Copy your github repository's link and paste after **?template=** in this link `https://www.heroku.com/deploy/?template=`. Like this:-


   `https://www.heroku.com/deploy/?template=https://github.com/whitehatjrchintu/flipkartpricechecker`

### Step 5:
- Now enter App name in app_name and api_id,api_hash and bot_token which you saved in above steps, in respective asked field. Then click **Deploy app**.

### Step 6:
- Your app now created. Go to your app settings. Here `https://dashboard.heroku.com/apps/your_heroku_app/settings`,click on **add buildpack** and add following 2 links one by one.

`https://github.com/heroku/heroku-buildpack-chromedriver`

`https://github.com/heroku/heroku-buildpack-google-chrome`

### Step 7:
- Now go here [dashboard.heroku.com/apps/your_heroku_app/deploy/github](https://dashboard.heroku.com/apps/your_heroku_app/deploy/github), click on **Deployment method** and connect your github account. Under **Search for a repository to connect to** enter your created repository's name (which you created at step3) and connect your repository. Then click **deploy branch** under **Manual deploy** section.

### Step 8:
- Finally go to your bot,click start button you will get notification exactly after 30 minutes.

## Note:-
- Replace your product url in **bot.py**.
- Do as per steps.
- I know they are some extra steps in it. I have to write this for noobs.
- I know they are extra things in **bot.py**. Will improve it soon.
- Meant for educational purpose only. I am not responsible if telegram block your account.