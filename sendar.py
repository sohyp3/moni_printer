import telegram
import api

bot = telegram.Bot(api.bot_api)

def messagu(msg):
    bot.sendMessage(chat_id= -1001296601205,text= msg)