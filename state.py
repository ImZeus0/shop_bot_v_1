from aiogram.dispatcher.filters.state import StatesGroup, State


class Donate(StatesGroup):
    enter_ammount = State()
    send_request = State()

class Add_file(StatesGroup):
    enter_cat = State()
    enter_price = State()