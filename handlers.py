from loader import bot, dp
from inline_keyboard import *
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext
from pay import startpayment
from database import *
from keyboard import *
from state import *
import logging
from aiogram.types.callback_query import CallbackQuery
from loader import _


@dp.message_handler(commands=['check'])
async def status_bot(m: Message):
    await m.answer('bot worked!')


@dp.message_handler(commands=['start'])
async def login_user(m: Message):
    id_refferal = m.get_args()
    res = check_user_in_db(m.chat.id)
    if res == None:
        await m.answer(_("Выберете язык / Choose languade"), reply_markup=lang_menu(id_refferal))
    else:
        await m.answer(_("Привет!"), reply_markup=main_menu)


@dp.message_handler(commands=['n'])
async def nickname(m: Message):
    add_pays(m.chat.id, 50)
    await m.answer("Пополнено 50")

@dp.message_handler(commands=['c'])
async def add_c(m: Message):
    print("+")
    name = m.text.split(' ')[1]
    add_category(name)
    await m.answer(f"Категория {name} добавлена")

@dp.message_handler(commands=['s'])
async def show(m: Message):
    cate = get_categorus()
    msg = ""
    for cat in cate:
        msg+=cat['name']+" "
    await m.answer(msg)

@dp.message_handler(content_types=['document'])
async def file(m: Message,state: FSMContext):
    file_name = m.document.file_name
    link = m.document.file_id
    cat = get_categorus()
    await state.update_data(file_name=file_name,link=link)
    await m.answer(m.document.file_name,reply_markup=add_file_button(cat))
    await Add_file.enter_cat.set()


@dp.callback_query_handler(choose_lang.filter())
async def select_lang(call: CallbackQuery, callback_data: dict):
    lang = callback_data.get('la')
    id_ref = int(callback_data.get('ref'))
    id_user = call.message.chat.id
    nickname = None
    try:
        nickname = call.from_user.username
    except:
        pass
    add_user(id_user, lang, nickname, id_ref)
    await call.message.answer("Пользователь добавлен ", reply_markup=main_menu)

@dp.message_handler(state=Add_file.enter_price)
async def set_price(m:Message,state: FSMContext):
    price = int(m.text)
    file_name = await state.get_data("file_name")
    link = await state.get_data("link")
    category = await state.get_data("category")
    add_product(file_name,category,price,link)
    await m.answer("Файл добавлен")
    await state.finish()



@dp.message_handler(content_types=['text'])
async def main(m: Message):
    if m.text == _("👤 Мой профиль"):
        bot_username = (await bot.get_me()).username
        id_user = m.chat.id
        bot_link = 'http://t.me/{bot_name}?start={id_user}'.format(bot_name=bot_username, id_user=m.chat.id)
        user = get_user(id_user)
        await m.answer(_(
            "<b>ЛИЧНИЙ КАБИНЕТ</b>\n\nID {id}\nБаланс {balance}\n"
            "Количество рефералов {referrals}\nРеферальная ссылкa {ref_link}\n"
            "Дата регистрации {date}").format(
            id=m.chat.id,
            balance=user['balance'],
            referrals=count_ref(id_user)['COUNT(*)'],
            ref_link=bot_link,
            date=user['date_reg']
        ), reply_markup=account_menu(id_user))
    elif m.text == _("🔥 Актуальний товар"):
        cate = get_categorus()
        await m.answer(_("Выберете категорию"),reply_markup=categoru_button(cate))
    elif m.text == _("🆘 Support"):
        pass
    elif m.text == _("❗️FAQ"):
        pass


@dp.callback_query_handler(text_contains="choose_donate")
async def donate(call: CallbackQuery):
    await call.answer(cache_time=60)
    id_user = call.message.chat.id
    await call.message.edit_text(_("Выберете тип оплати"))
    await call.message.edit_reply_markup(choose_donate(id_user))

@dp.callback_query_handler(text_contains="addfile")
async def add_file(call : CallbackQuery,state: FSMContext):
    category = call.data.split("_")[1]
    await state.update_data(category=category)
    await call.message.answer("Введите цену $")
    await Add_file.enter_price.set()



@dp.callback_query_handler(donate_btc.filter())
async def donate_btc(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.edit_text(_("Введите сумму $"))
    await state.update_data(id_user=call.message.chat.id)
    await Donate.enter_ammount.set()


@dp.message_handler(state=Donate.enter_ammount)
async def enter_ammount(m: Message, state: FSMContext):
    elem = await state.get_data()
    id_user = elem['id_user']
    ammount = int(m.text)
    url_pay = startpayment(ammount, id_user)
    await m.answer(_("Нажмите на кнопку чтобы оплатить"), reply_markup=buy_btc(url_pay, ammount))
    await state.finish()


@dp.callback_query_handler(text_contains='donate_back')
async def close_donate(call: CallbackQuery):
    await call.answer(cache_time=60)
    id_user = call.message.chat.id
    user = get_user(id_user)
    balance = user['balance']
    date = user['date_reg']
    referrals = count_ref(id_user)['COUNT(*)']
    await call.message.edit_text(_(await account_info(id_user, balance, referrals, date)))
    await call.message.edit_reply_markup(reply_markup=account_menu(id_user))


async def account_info(id_user, balance, referrals, date):
    bot_username = (await bot.get_me()).username
    bot_link = 'http://t.me/{bot_name}?start={id_user}'.format(bot_name=bot_username, id_user=id_user)
    return "<b>ЛИЧНИЙ КАБИНЕТ</b>\n\nID {id}\nБаланс {balance}\nКоличество рефералов {referrals}\nРеферальная ссылкa {ref_link}\nДата регистрации {date}".format(
        id=id_user,
        balance=balance,
        referrals=referrals,
        ref_link=bot_link,
        date=date

    )



