import telebot

token = "7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM"
bot = telebot.TeleBot(token)

# ////
@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, ' Start!')

@bot.message_handler(content_types=['text'])
def bot_message_text(message):
    mes = message.text + '\nДовжина повідомлення: ' + str(len(message.text)) + ' символів.'
    bot.send_message(message.chat.id, mes)


if __name__ == '__main__':
    bot.polling()