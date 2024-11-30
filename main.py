import telebot
from telebot import types

token = '7688946735:AAHssgKXxiknVKQK-F6gQTyv6_MD8mfAeG0'
bot = telebot.TeleBot(token)


stickers = ['CAACAgIAAxkBAAMoZ0rf8E7elq5ul1UK9Nesef1NXC4AAiEAA61lvBQ6o52_217jSDYE']

# --- BOT MESSAGE ---------------------------------------------------

# bot comands

@bot.message_handler(commands=['stop'])
def command_stop(message):
    bot.send_message(message.chat.id, 'command STOP')

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'command START')

# кманда починається з символа: /open, /close
@bot.message_handler(commands=['open', 'close'])
def commands_open_close(message):
    mes = 'error'

    if message.text == '/open':
        mes = 'відкрито'
    elif message.text == '/close':
        mes = 'закрито'

@bot.message_handler(commands=['key'])
def key_go(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton(text='кнопка 1')
    button2 = types.KeyboardButton(text='кнопка 2')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, 'клавіатура', reply_markup=keyboard)

# реакція на кнопки
@bot.message_handler(func=lambda message: message.text == 'кнопка 1')
def handle_button_1(message):
    bot.send_message(message.chat.id, 'ви натиснули кнопку 1')

@bot.message_handler(func=lambda message: message.text == 'кнопка 2')
def handle_button_1(message):
    bot.send_message(message.chat.id, 'ви натиснули кнопку 2')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji
    bot.reply_to(message,f"ви надіслали стікер з емоджі {emoji} (ID: {sticker_id})")


# --- TEXT ---

@bot.message_handler(content_types=['text'])
def bot_message(message):

    if message.text == '1':
        bot.send_sticker(message.chat.id, stickers[0])
        return True

    mes = message.text + ' - Це просто текст'
    bot.send_message(message.chat.id, mes)




# --- Функції -------------------------------------------------------

# Додаємо кнопки
def bot_buttons(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='Кнопка 1')
    button_2 = types.KeyboardButton(text='Кнопка 2')
    button_3 = types.KeyboardButton(text='Кнопка 3')
    button_4 = types.KeyboardButton(text='Кнопка 4')
    keyboard.add(button_1, button_2, button_3, button_4)

    msg = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)


def button_if(message):
    if message.text == 'Кнопка 1':

        # ... запустити програму ...
        bot.send_message(message.chat.id, '1. Закопати путіна')
    elif message.text == 'Кнопка 2':
        bot.send_message(message.chat.id, '2. Закопати шойгу')
    else:
        bot.send_message(message.chat.id, '3,4. запустити русоріз')


if __name__ == '__main__':
    bot.polling()
