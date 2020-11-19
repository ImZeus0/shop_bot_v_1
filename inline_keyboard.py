from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from callback import *
from loader import _

def account_menu(id_user):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(_("Попоплнить баланс"),callback_data='choose_donate')],
        [InlineKeyboardButton(_("История покупок"), callback_data=history_pays.new(id_user=id_user))],
    ])
    return kb

def choose_donate(id_user):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(_("Криптовалюта"),callback_data=donate_btc.new(id_user=id_user))],
        [InlineKeyboardButton("QIWI", callback_data=donate_qiwi.new(id_user=id_user))],
        [InlineKeyboardButton(_("Назад"), callback_data='donate_back')]
    ])
    return kb