from telegram.ext import * 
import telegram

import api

# in respones file there is sample_response which takes the text and the date of the message
# it has the replies

import respones as R 

bot = telegram.Bot(api.bot_api)

# To send messages Currently inactive
def messagu(msg):
    bot.sendMessage(chat_id= -1001248147733,text= msg)

# Command replies (/start)
def start_command(update,context):
    update.message.reply_text('type somtin')

# Command replies (/help)
def hilp_cmd(update,context):
    update.message.reply_text('Do i look like google?')

# Messae Handler/ txt is the text from teleram / dateu is the date of the message
# R as i imported at the first is a file with responses
def handle_message(update, context):
    txt = str(update.message.text)
    dateu = update.message.date
    response = R.sample_response(txt,dateu)
    update.message.reply_text(response)

# Caption Handler (the text under the photo)
def caoto(update,context):
    txt2 = str(update.message.caption)
    dateu = update.message.date
    response = R.sample_response(txt2,dateu)
    update.message.reply_text(response)

# error handler
def error(update,context):
    print(f"Update {update} caused error {context.error} idiot")

def main():
    print('bot started plz work')
    updater = Updater(api.bot_api, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',hilp_cmd))  

    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_handler(MessageHandler(Filters.caption,caoto))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
