from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    update.message.reply_text("سلام! به ربات خوش آمدید 👋")

def main():
    updater = Updater("7717521795:AAFC65Hb0CLAGGYiRiEoZcUSaK8JjjZeuFA", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
