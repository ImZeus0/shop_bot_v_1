from loader import bot,dp
from inline_keyboard import *
from  aiogram.types import Message,ContentType
from keyboard import *
import logging
from loader import _

@dp.message_handler(commands=['check'])
async def status_bot(m:Message):
    await m.answer('bot worked!')


@dp.message_handler(commands=['start'])
async def login_user(m:Message):
    await m.answer(_("Привет!\nЭто описания твоего бота"),reply_markup=main_menu)

@dp.message_handler(content_types=['text'])
async def main_menu(m:Message):
    if m.text == _("👤 Мой профиль"):
        bot_username = (await bot.get_me()).username
        id_user = m.chat.id
        bot_link = 'http://t.me/{bot_name}?start={id_user}'.format(bot_name=bot_username,id_user=m.chat.id )
        await m.answer(_("<b>ЛИЧНИЙ КАБИНЕТ</b>\n\nID {id}\nБаланс {balance}\nКоличество рефералов {referrals}\nРеферальная ссылкa {ref_link}").format(
            id=m.chat.id,
            balance=100101,
            referrals = 0000,
            ref_link = bot_link
        ),reply_markup=account_menu(id_user))
    elif m.text == _("🔥 Актуальний товар"):
        pass
    elif m.text == _("🆘 Support"):
        pass
    elif m.text == _("❗️FAQ"):
        pass

@dp.callback_query_handler(text_contains="choose_donate")
async def choose_donate(call:CallbackQ):