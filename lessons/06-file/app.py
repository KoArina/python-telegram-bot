import telebot

token = "7688946735:AAHssgKXxiknVKQK-F6gQTyv6_MD8mfAeG0"
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