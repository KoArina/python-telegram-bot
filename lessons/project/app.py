from urllib.response import addbase

from telebot.types import InlineKeyboardMarkup

import config as c
import telebot
import threading
import time
import sqlite3
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(c.TOKEN)

USER_CHAT_ID = '6161170582'

## SQLITE3 ========================================================
# db = sqlite3.connect('notebook.db')
# cursor = db.cursor()
#
# cursor.execute('''CREATE TABLE users (
#      id INTEGER PRIMARY KEY,
#      chat_id INTEGER NOT NULL UNIQUE,
#      name TEXT DEFAULT 'Unknown',
#      deleted INTEGER DEFAULT 1
#      )''')
# db.commit()
#
# cursor.execute('''CREATE TABLE notes (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      user_id INTEGER NOT NULL,
#      title TEXT NOT NULL,
#      content INTEGER DEFAULT '',
#      notification DATETIME DEFAULT CURRENT_TIMESTAMP,
#      is_send INTEGER DEFAULT 0,
#      deleted INTEGER DEFAULT 1
#      )''')
# db.commit()

# FUNCTION ==============================================================
def send_stupid_message():
    while True:
        bot.send_message(USER_CHAT_ID, 'дурне повідомлення')
        time.sleep(10)
def add_note(message):
    bot.send_message(message.chat.id, "введіть нотатку:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, save_note)

def save_note(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
    row = cur.fetchone()

    if row:
        cur.execute("INSERT INTO notes (user_id, title) VALUES(?, ?)",
                    (row[0], message.text))
        db.commit()
        bot.send_message(message.chat.id, 'нотатку збережено')
    cur.close()
    db.close()


def show_all_notes(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
    row = cur.fetchone()

    if row:
        cur.execute(f"SELECT id, title, notification  FROM notes WHERE deleted=1 AND user_id={row[0]}")
        rows = cur.fetchall()

        notes = 'список нотаток:\n\n'
        for r in rows:
            notes += f"/open_{r[0]}: {r[1]}. [{r[2]}]\n"

        bot.send_message(message.chat.id, notes)

    cur.close()
    db.close()

def bot_start(message):
    print(message)
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("SELECT chat_id FROM users WHERE chat_id='{0}'".format(message.chat.id))
    row = cur.fetchone()

    if not row:
        cur.execute(f"INSERT INTO users (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
        db.commit()
        bot.send_message(message.chat.id, 'вас додано до цього бота')
    else:
        bot.send_message(message.chat.id, 'Ви вже підписані на цього бота')

def open_note(message, note_id):
    keyboard = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('нотатку', callback_data='/edit_' + note_id)
    b2 = InlineKeyboardButton('час', callback_data='/time_' + note_id)
    b3 = InlineKeyboardButton('видалити', callback_data='/delete_' + note_id)
    keyboard.add(b1, b2)
    keyboard.add(b3)

    bot.send_message(message.chat.id, 'редагувати: ', reply_markup=keyboard)


def edit_note(message, note_id):
    pass

def time_note(message, note_id):
    pass

def delete_note(call, note_id):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("UPDATE notes SET deleted=0 WHERE id=%d"% int(note_id))
    db.commit()

    if cur.rowcount > 0:
        bot.send_message(call.message.chat.id, 'видалено')
    else:
        bot.send_message(call.message.chat.id, 'помилка видалення: ')

    cur.close()
    db.close()


# start - підписка
# add - додати
# edit - редагувати
# del - видалити
# all - показати всі
# day - показати за день
# end - відписатись

@bot.message_handler(commands=['start', 'add', 'all', 'day', 'end'])
def handler_text_message(message):
    if '/start' == message.text:
        bot_start(message)
    elif '/add' == message.text:
        add_note(message)
    elif '/all' == message.text:
        show_all_notes(message)
    elif '/day' == message.text:
        pass
    elif '/end' == message.text:
        pass

@bot.message_handler(regexp=r"^\/open_\d+$")
def handler_edit_id(message):
    values = message.text.split('_')
    open_note(message, values[1])


@bot.callback_query_handler(func=lambda call: True)
def handler_note_action(call):
    values = call.data.split('_')
    if 2 == len(values):
        if '/delete' == values[0]:
            delete_note(call, values[1])
        elif '/edit' == values[0]:
            pass
        elif '/time' == values[0]:
            pass

@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    # print(message.chat.id)
    bot.send_message(message.chat.id, 'працює ' + str(message.chat.id))

if __name__ == "__main__":
#    thread = threading.Thread(target=send_stupid_message)
#    thread.start()
    # запуск бота
    bot.infinity_polling()