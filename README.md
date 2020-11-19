# Flipkart price checker/monitoring telegram bot.

With this telegram bot you can monitor price of any Flipkart product. This TG bot is **heroku** based. Now before you continue i recommend you to read [**Note**](https://github.com/whitehatjrchintu/flipkartpricechecker#note-) section.

## Example:-

![example](https://i.ibb.co/fQJVGTF/example.jpg "example")

## Prerequisites:-

1. Create account on [GitHub](https://www.github.com) (if you haven't).
2. Create account on [Heroku](https://dashboard.heroku.com) (if you haven't).
3. Create account on [Telegram](https://web.telegram.org) (if you haven't).
4. Create account on [Gmail](https://mail.google.com) (if you haven't for only this script).
5. Go to [my.telegram.org/auth](https://my.telegram.org/auth), login and create app. Check [how to create app on telegram](https://core.telegram.org/api/obtaining_api_id). Now save api_id and api_hash which you got from [my.telegram.org/auth](https://my.telegram.org/auth).
6. Create a telegram bot by using [Bot Father](https://t.me/botfather). Check [how to create bot in telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot). [Bot Father](https://t.me/botfather) will give you bot token save that token.
7. Allow [less secure apps to access](https://devanswers.co/allow-less-secure-apps-access-gmail-account/) to your above created gmail account.
8. So now you have saved **three** things:-
- api_id
- api_hash
- bot_token
- gmail credentials

## How to use?
### Step 1:
- Just git clone this repository and start working by editing the code.

   `git clone https://github.com/whitehatjrchintu/flipkartpricechecker.git`
   `cd flipkartpricechecker`

- Or download this [repository](https://github.com/whitehatjrchintu/flipkartpricechecker/archive/main.zip) as zip.
  
### Step 2:
- After cd or unzip you have to edit **bot.py** file.

- In bot.py **teri_chat_id_daal** this mentioned two times. You have to replace this with your chat id. Search **@chatid_echo_bot** in telegram (This bot is not mine. You can google how to get chat id in telegram.) and click start this will give you your chat id. Now replace **teri_chat_id_daal** with your chat id number.

- Enter gmail credentials in [line 40](https://github.com/whitehatjrchintu/flipkartpricechecker/blob/028c12afe6990abdd20f64d8c34b0b7e878deebe/bot.py#L40), enter sender email,receiver email in line [line 44](https://github.com/whitehatjrchintu/flipkartpricechecker/blob/028c12afe6990abdd20f64d8c34b0b7e878deebe/bot.py#L44).

- Make other changes like url,subject etc. at your own if you want to change.

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
- I know there is some extra steps in it. I have to write this for noobs.
- Will improve it timely. If "pro's" found any mistake or any suggestion let me know i will correct it.
- Meant for educational purpose only. I am not responsible if telegram block your account.

# Updates:-
- Added smtp for sending emails if price decreases at a particular mentioned level. (19-11-2020)
