import time

import telebot
from telebot.types import Message

TOKEN = '1053642045:AAFip4Fj57gAhYAAAZLH-XWwx0u6RYfmNag'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Введите текст шпоры и заблокируйте телефон')


@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    txt = message.text
    et1 = txt[0:210]
    et2 = txt[210:420]
    et3 = txt[420:630]
    et4 = txt[630:840]
    et5 = txt[840:1050]
    time.sleep(3)
    bot.send_message(message.chat.id, et1)
    time.sleep(3)
    if et2 != "":
        bot.send_message(message.chat.id, et2)
    time.sleep(3)
    if et3 != "":
        bot.send_message(message.chat.id, et3)
    time.sleep(3)
    if et4 != "":
        bot.send_message(message.chat.id, et4)
    time.sleep(3)
    if et5 != "":
        bot.send_message(message.chat.id, et5)


bot.polling(timeout=60)