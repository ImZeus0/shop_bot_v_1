from loader import bot,dp
from inline_keyboard import *
from  aiogram.types import Message,ContentType
from aiogram.dispatcher import FSMContext
from keyboard import *
from state import Donate
import logging
from aiogram.types.callback_query import CallbackQuery
from loader import _

@dp.message_handler(commands=['check'])
async def status_bot(m:Message):
    await m.answer('bot worked!')


@dp.message_handler(commands=['start'])
async def login_user(m:Message):
    await m.answer(_("Привет!\nЭто описания твоего бота"),reply_markup=main_menu)

@dp.message_handler(content_types=['text'])
async def main(m:Message):
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
async def donate(call:CallbackQuery):
    await call.answer(cache_time=60)
    id_user = call.message.chat.id
    await call.message.edit_text(_("Выберете тип оплати"))
    await call.message.edit_reply_markup(choose_donate(id_user))

@dp.callback_query_handler(donate_btc.filter())
async  def donate_btc(call:CallbackQuery,callback_data : dict,state :FSMContext):
    await call.answer(cache_time=60)
    id_user = int(callback_data.get('id_user'))
    await call.message.edit_text(_("Введите сумму $"))
    await state.update_data(id_user = call.message.chat.id)
    await Donate.enter_ammount.set()

@dp.message_handler(state=Donate.enter_ammount)
async  def enter_ammount(m: Message,state :FSMContext):
    elem = await state.get_data()
    await m.edit_text(elem['id_user'])
    await state.finish()

@dp.callback_query_handler(state=Donate.send_request)
async  def enter_ammount(call: CallbackQuery,state :FSMContext):
    await call.answer(cache_time=60)
    elem = await state.get_data()
    await call.message.edit_text()
    await  state.finish()


@dp.callback_query_handler(text_contains='donate_back')
async def close_donate(call:CallbackQuery):
    id_user = call.message.chat.id
    balance = 0
    referrals = 0
    await call.message.edit_text(_(await account_info(id_user,balance,referrals)))
    await call.message.edit_reply_markup(reply_markup=account_menu(id_user))


async def account_info(id_user,balance,referrals):
    bot_username = (await bot.get_me()).username
    bot_link = 'http://t.me/{bot_name}?start={id_user}'.format(bot_name=bot_username, id_user=id_user)
    return "<b>ЛИЧНИЙ КАБИНЕТ</b>\n\nID {id}\nБаланс {balance}\nКоличество рефералов {referrals}\nРеферальная ссылкa {ref_link}".format(
        id=id_user,
        balance=balance,
        referrals=referrals,
        ref_link=bot_link
    )