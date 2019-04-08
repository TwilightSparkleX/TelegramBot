import telebot

token = '601516197:AAG9PIsBH_zQRq3RJfv6svoLfhOKzkdYOB4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.polling()