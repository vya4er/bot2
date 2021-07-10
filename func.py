from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from random import randint
from const import *
import time

def start(update, context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    top_button = [KeyboardButton(text='Нажми меня')]
    mid_button = [KeyboardButton(text='Нажми меня 2')]
    bot_button = [KeyboardButton(text='Нажми меня 3')]
    lang_buttons = InlineKeyboardButton(text='Русский', callback_data='rus'), InlineKeyboardButton(text='Узбекский',
                                                                                                   callback_data='uzb')
    context.bot.send_message(chat_id=user_id, text='Привет {}'.format(name), reply_markup=InlineKeyboardMarkup([lang_buttons]))
    datetime = time.asctime()
    logpath = 'logs.txt'
    log = open(logpath, 'a')
    log_str = '{}, {}, {}, {}\n'.format(datetime, user_id, name, '/start')
    log.writelines(log_str)
    log.close()

def text_answer(update, context):
    user_id = update.message.chat_id
    text = update.message.text
    text = text.lower()
    if text in DCT.keys():
        context.bot.send_message(chat_id=user_id, text=(DCT.get(text)[randint(0, 2)]))
    else:
        datetime = time.asctime()
        logpath = 'logs.txt'
        log = open(logpath, 'a')
        log_str = '{}, {}, {}\n'.format(datetime, user_id, text)
        log.writelines(log_str)
        log.close()
def rus (update,context):
    user_id = update.callback_querry.from_user.id
    context.bot.send_message (chat_id-user_id, text='Выбран русскйи язык')
def uzb (update,context):
    user_id = update.callback_querry.from_user.id
    context.bot.send_message (chat_id-user_id, text='Выбран узбекский язык')
