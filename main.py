import telebot

token = '7816150863:AAEGVVNY7J5WayCc3iqIaaisdp43LbDTnY'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def botmessage(message):
    mes = message.text + ' - Це написала класна дівчинка'
    bot.send_message(message.chat.id, mes)


bot.polling()