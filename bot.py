import telebot

bot = telebot.TeleBot('7717521795:AAFC65Hb0CLAGGYiRiEoZcUSaK8JjjZeuFA')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات خوش آمدید 👋")

bot.polling()
