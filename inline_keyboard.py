from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from callback import *
from loader import _

def account_menu(id_user):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(_("Попоплнить баланс"),callback_data=choose_donate_callback.new(id_user=id_user))],
        [InlineKeyboardButton(_("История покупок"), callback_data=history_pays.new(id_user=id_user))],
    ])
    return kb