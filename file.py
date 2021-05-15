from telegram.ext import * 
import telegram

import api

import respones as R 

bot = telegram.Bot(api.bot_api)

def messagu(msg):
    bot.sendMessage(chat_id= -1001248147733,text= msg)

def start_command(update,context):
    update.message.reply_text('type somtin')


def hilp_cmd(update,context):
    update.message.reply_text('Do i look like google?')

    
def handle_message(update, context):
    txt = str(update.message.text)
    dateu = update.message.date
    response = R.sample_response(txt,dateu)
    update.message.reply_text(response)

def caoto(update,context):
    txt2 = str(update.message.caption)
    # update.message.reply_text("work mf")
    dateu = update.message.date

    response = R.sample_response(txt2,dateu)
    update.message.reply_text(response)
    
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
