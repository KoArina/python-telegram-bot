import telebot

token = "7688946735:AAHssgKXxiknVKQK-F6gQTyv6_MD8mfAeG0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['file'])
def read_file(message):
    try:
        with open('bot.txt') as file:
            info = file.read()
    except FileNotFoundError:
        with open('bot.txt', 'w') as file:
            file.write('')

    bot.send_message(message.chat.id, '1')


@bot.message_handler(content_types=['file'])
def read_file(message):
    with open('bot.txt', 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'бот працює.')


if __name__ == '__main__':
        bot.infinity_polling()
