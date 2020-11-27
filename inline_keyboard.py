from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback import *
from loader import _


def account_menu(id_user):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(_("Попоплнить баланс"), callback_data='choose_donate')],
        [InlineKeyboardButton(_("История покупок"), callback_data=history_pays.new(id_user=id_user))],
    ])
    return kb


def lang_menu(id_ref):
    if id_ref == "":
        kb = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(_("🇷🇺 Rus"), callback_data=choose_lang.new(la='ru', ref='0')),
                              InlineKeyboardButton(_("🇬🇧 Eng"), callback_data=choose_lang.new(la='en', ref='0'))]])
    else:
        kb = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(_("🇷🇺 Rus"), callback_data=choose_lang.new(la='ru', ref=id_ref)),
                              InlineKeyboardButton(_("🇬🇧 Eng"), callback_data=choose_lang.new(la='en', ref=id_ref))]])
    return kb


def choose_donate(id_user):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(_("Криптовалюта"), callback_data=donate_btc.new(id_user=id_user))],
        [InlineKeyboardButton("QIWI", callback_data=donate_qiwi.new(id_user=id_user))],
        [InlineKeyboardButton(_("Назад"), callback_data='donate_back')]
    ])
    return kb


def buy_btc(url, ammount):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(_("Оплатить {ammount}$").format(ammount=str(ammount)),
                                               url=url)]])
    return kb

def categoru_button(cat):
    arr = []
    for c in cat:
        name = c['name']
        arr.append([InlineKeyboardButton(name,callback_data="categoru_"+name)])
    kb = InlineKeyboardMarkup(inline_keyboard=arr)
    return kb

def add_file_button(cat):
    arr = []
    for c in cat:
        name = c['name']
        arr.append([InlineKeyboardButton(name, callback_data="addfile_" + name)])
    kb = InlineKeyboardMarkup(inline_keyboard=arr)
    return kb
