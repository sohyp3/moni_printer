from telegram.ext import * 

import api

import respones as R 

def start_command(update,context):
    update.message.reply_text('type somtin')


def hilp_cmd(update,context):
    update.message.reply_text('Do i look like google?')

    
def handle_message(update, context):
    txt = str(update.message.text).lower()
    response = R.sample_response(txt)
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
    
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
