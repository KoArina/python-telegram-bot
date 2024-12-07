import telebot
from telebot import types
import os

token = "7688946735:AAHssgKXxiknVKQK-F6gQTyv6_MD8mfAeG0"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def say_number(message):
    if message.text == '1':
        request = 'one'
    elif message.text == '2':
        request = 'two'
    elif message.text == '3':
        request = 'three'
    elif message.text == '4':
        request = 'four'
    elif message.text == '5':
        request = 'five'
    else:
        request = 'не знайдено'

    bot.send_message(message.chat.id, request)

if __name__ == '__main__':
    bot.polling()
